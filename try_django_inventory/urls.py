"""try_django_inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include
from django.contrib import admin
from django.urls import path
from .views import home
from articles import views as article_views
from accounts import views as account_views
urlpatterns = [
    path('', home, name="home"),
    path('pantry/recipes/', include('recipes.urls')),
    path('articles/', include('articles.urls')),
    path('login/', account_views.login_view, name='login'),
    path('register/', account_views.register_view, name='registration'),
    path('logout/', account_views.logout_view, name="logout"),
    path('admin/', admin.site.urls)
]
