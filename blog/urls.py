from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView


app_name = BlogConfig.name

urlpatterns = [
    path('', BlogPostListView.as_view(), name='list'),
    path('create/', BlogPostCreateView.as_view(), name='create'),
    path('edit/<slug>', BlogPostUpdateView.as_view(), name='edit'),
    path('view/<slug>', BlogPostDetailView.as_view(), name='view'),
    path('delete/<slug>', BlogPostDeleteView.as_view(), name='delete'),
]
