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
