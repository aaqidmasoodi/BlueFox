# form validation next
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    # mention what model you are working with 
    # the fields that you are interested in 
    # that is all