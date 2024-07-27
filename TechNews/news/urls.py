from django.urls import path
from .views import (
    NewsListCreateAPIView,
    TagsListCreateAPIView,
    ResourcesListCreateAPIView
)

app_name = 'news'

urlpatterns = [
    path('news/', NewsListCreateAPIView.as_view(), name='news-list-create'),
    path('tags/', TagsListCreateAPIView.as_view(), name='tags-list-create'),
    path('resources/', ResourcesListCreateAPIView.as_view(), name='resources-list-create'),
]
