from django.urls import path
from . import views

urlpatterns = [
    path("blogposts/create/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(), name="update"),
    path("blogposts/", views.BlogPostList.as_view(), name="blogpost-list-view")
]
