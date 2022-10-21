from django.test import TestCase, Client
from user_posts.models import User_Post
from .serializers import PostSerializer
from rest_framework import status
from django.contrib.auth.models import User




