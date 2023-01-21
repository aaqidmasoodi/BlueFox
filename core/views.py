from django.shortcuts import render, redirect
from core.models import Post # step 1 - bring in the model

# here is where we can pass "stuff" -->> data into the template

# if a route is protected
# you can either create a must authenticate page or redirect them to the login
def home_view(request):

    if not request.user.is_authenticated:
        return redirect("login")


    # step 2
    # fetch data from the (table or Model)
    posts = Post.objects.all()

    # create the context
    context = {
        "posts":posts,
    }

    #                                         pass the context into the template
    return render(request, 'core/index.html', context)

def contact_view(request):

    return render(request, 'core/contact.html')

def about_view(request):

    return render(request, 'core/about.html')
