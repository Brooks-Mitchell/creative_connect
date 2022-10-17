from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth.models import User
from .models import User_Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Post
        fields = '__all__'
        
        #fields = ['id', 'title', 'date_posted', 'author']

    
