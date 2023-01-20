from django.db import models

# Creating Blogpost model with title and desc fields.
class Blogpost(models.Model):
    title = models.CharField(max_length= 150)
    desc = models.TextField()  