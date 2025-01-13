from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
  class Meta:
    model = BlogPost
    # Fields specified here will be serialized and returned in the API.
    # id is automatically created in the model.
    fields = ["id", "title", "content", "published_date"]
