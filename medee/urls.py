# news/urls.py

from django.urls import path
from .views import NewsListView, NewsDetailView

urlpatterns = [
    path('news/', NewsListView.as_view(), name='news-list'),  # List of all news
    path('news/<int:id>/', NewsDetailView.as_view(), name='news-detail'),  # Specific news by id
]
