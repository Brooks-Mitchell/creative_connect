"""creative_connect_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from user_posts.views import PostList
from users.views import UserDetail, UserList, UserCreate
from users.views import front


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', front, name="front"),
    path('posts/', PostList.as_view()),

    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),

    path('user-auth/', include('rest_framework.urls')),

    path('create-account/', UserCreate.as_view(), name='create-account'),
]
