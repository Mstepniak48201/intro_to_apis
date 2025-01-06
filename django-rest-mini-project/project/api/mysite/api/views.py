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

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # Copy the queryset and serializer.
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    # pk is "primary key," which is the id of the blogpost.
    lookup_field = "pk"


