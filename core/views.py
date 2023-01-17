from django.shortcuts import render, HttpResponse



def home_view(request):

    return render(request, 'core/index.html')

def contact_view(request):

    return render(request, 'core/contact.html')

def about_view(request):

    return render(request, 'core/about.html')
