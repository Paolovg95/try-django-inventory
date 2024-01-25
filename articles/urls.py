from django.urls import path
from .views import (
    articles_search_view,
    article_create_view,
    article_detail_view,
)


app_name="articles"
urlpatterns =[
    path('', articles_search_view),
    path('create/', article_create_view, name='create'),
    path('<slug:slug>/', article_detail_view, name="detail"),
]