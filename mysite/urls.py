from django.contrib import admin
from django.urls import path, include

# 127.0.0.1:8000/
# a-asdfasdfas f/blog/create/4
# www.patrick.com/
urlpatterns = [
    path('admin/', admin.site.urls), # this route is there by default
    path('', include('core.urls'))
]

