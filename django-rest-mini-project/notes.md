# Django REST API mini project

## Setup

- Make project directory

- Make requirements.txt

```
requirements.txt

django
djangorestframework
environs
```

- Install dependencies: Run:
pip3 install -r requirements.text

- Create new Django project: Run:
django-admin startproject mysite
  
// If the above command doesn't work, try:
python3 -m django startproject mysite

// This should create a new directory called "mysite."
// This is where we will write the API.
cd mysite

- Create app: Run:
// Notice within the mysite directory, there is a file manage.py. This will help us create the app.
// The command startapp in manage.py takes a name arg. We will name the ap "api."
python3 manage.py startapp api

// A new directory called api should be created within mysite.
// Project structure should look like this:

```
project_root_directory
  - mysite
    - api
    - mysite
    - manage.py
    - requirements.txt
```


## Connecting the app with the Django project

// cd into the app directory
cd mysite/mysite

open settings.py -> scroll to INSTALLED APPS = []
  - Add our app to the list of installed apps.
  - The app should be called "api" so we just add "api" to the list.
  - Additionally, we will add the Django REST framework to the installed apps list.
    - Add `"rest_framework"` to the list.


## Building the model that our data will interact with

cd api

open models.py

Django uses ORM: Object Relational Mapping.

ORM maps a Python Object to an Instance of a Database. This allows us to use multiple types of databases, and Django handles all of the low level commands that create, update and retrieve data. The ORM is a higher level wrapper.

```
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
```


## Defining the Serializer

For now, we will be treating the Serializer as a black box that converts our data model into JSON. Further study will focus on customizing and extending it. Here, it will take the model that we just defined, and convert it into JSON compatiable data that the API can interact with.

This will use the Meta class, which is common to Django and Django Rest Framework. It is used to define metadata for a parent class.

- "Meta" is not a reserved word for this class, but it is convention and the Django framework is programmed to look for a class named Meta.

- The Meta class is where we specify additional configuration for the parent class

From within the api directory:

vim serializers.py

```

from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
  class Meta:
    model = BlogPost
    # Fields specified here will be serialized and  returned in the API.
    # id is automatically created in the model.
    fields = ["id", "title", "content", "published_date"]
```


## Creating Views

A view is a function or class that takes a web request and returns a response such as an HTML page, JSON, or error.

A view is where the logic for handling requests and returning responses is defined. Views take user requests and decide what data to fetch, how to format it, and what to send back. In Django REST Framework, views work with serializers to format data, and with models to retrieve data. Views are the brain of the API that connects requests to the correct data and ensures it is in the correct format when returned.

We are going to import generics from `rest_framework`, which will give us the "generic view," which is a pre-built class that handles a lot of typical API tasks, such as listing, retrieving, creating, updating, deleting. 

Create a view that utilizes the model and the serializer.

From the api directory, go to views.py

```
from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer 

# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
  # Get all BlogPost objects that exist using the ORM.
  queryset = BlogPost.objects.all()

  # Specify which serializer we want to use.
  serializer_class = BlogPostSerializer 



```








