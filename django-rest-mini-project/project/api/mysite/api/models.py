from django.db import models

# Create your models here.

# Inheriting from Model gives us the functionality of a table from a SQL database.
class BlogPost(models.Model):
  # Define the model's columns/fields, the type of information it will store.
  title = models.CharField(max_length=100)
  content = models.TextField()
  published_date = models.DateTimeField(auto_add_now=True)
  
  # So we can print() and see the title of the object.
  def __str__(self):
    return self.title 
