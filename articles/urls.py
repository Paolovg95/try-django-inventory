from django.urls import path
from .views import (
    articles_search_view,
    article_create_view,
    article_detail_view,
    article_hx_detail_view
)


app_name="articles"
urlpatterns =[
    path('', articles_search_view, name="hx-home"),
    path('create/', article_create_view, name='create'),
    path('<slug:slug>/', article_detail_view, name="detail"),
    path('hx/<slug:slug>/', article_hx_detail_view, name="hx-detail"),
]
