from django.contrib import admin
from core.models import Post


'''
After we create a (table or model)
we must register them here in order to see them in the
admin site.
'''

admin.site.register(Post)


'''
in the admin site you can see Post Object (1), Post Object (2) stuff
which is called the string representation of the object
>> to change that you must go to the model and add the __str__
'''