from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BlogPost
from .serializers import BlogPostSerializer 

# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    # Get all BlogPost objects that exist using the ORM.
    queryset = BlogPost.objects.all()

    # Specify which serializer we want to use.
    serializer_class = BlogPostSerializer 

    # Create function to override generic view and delete all blogposts.
    # Return HTTP_204_NO_CONTENT
    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # Copy the queryset and serializer.
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    # pk is "primary key," which is the id of the blogpost.
    lookup_field = "pk"

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Inherit from APIView to create a custom view.
class BlogPostList(APIView):
    def get(self, request, format=None):
        # Get title. If no title, title == "".
        title = request.query_params.get("title", "")

        if title:
            # Filter queryset based on title.
            blog_posts = BlogPost.objects.filter(title__icontains=title)
        else:
            # If no title, return all blogposts.
            blog_posts = BlogPost.objects.all()

        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


