from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout


User = get_user_model()


def login_view(request):


    # check if user is already authneicated 
    # if they are then redirect them to the home page
    if request.user.is_authenticated:
        return redirect("home")

    if request.POST:

        username = request.POST['username']
        password = request.POST['password1']


        # this function authenticate checks whether the user with 
        # the given username and password is in the dateabase or not
        user = authenticate(username=username, password=password)

        if user is not None:
            # users does exist
            print("users does really exist in the db")
            # instead just login the user
            login(request, user=user)

            # is_authenticated = True
            # user = user
            # id = user.id

            return redirect("home")

            # this function login create a session for the user
            # A backend authenticated the credentials
        else:
            # No backend authenticated the credentials
            print("User does not exist")



    return render(request, 'account/login.html')


def logout_view(request):
    logout(request)
    # this clears out everything from the 'request' 
    return redirect("home")




def signup_view(request):

    # check if user is already authneicated 
    # if they are then redirect them to the home page
    if request.user.is_authenticated:
        return redirect("home")

    print("Sign up view called..")

    # Another way to check the same way
    # if request.method == "POST":

    if request.POST:


        '''TODO
        validation using form 
        '''

        # the form method is much
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        passwordc = request.POSt['password2']
        # username = request.POST.get('username')
        user = User.objects.create_user(username, email, password)
        # this operation actually saves the user to the saves
        user.save()


        return redirect("home")


    return render(request, 'account/signup.html')