from django.shortcuts import render, HttpResponse
from core.models import Post # step 1 - bring in the model

# here is where we can pass "stuff" -->> data into the template
def home_view(request):

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
