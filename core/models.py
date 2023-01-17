from django.db import models


# creating a table to contain all the posts

# what it has  
# what to do 
class Post(models.Model):
    # add image field
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)

    # auto populate the time stamp
    date_posted = models.DateTimeField(auto_now_add=True)

    # author

    # whatever string is going to returned from this will be the string represenation
    def __str__(self):
        return self.title # ideally we return some info about the object