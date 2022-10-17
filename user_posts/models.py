from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class User_Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=320)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)