from rest_framework import serializers
from django.contrib.auth.models import User

from user_posts.models import User_Post

class UserSerializer(serializers.ModelSerializer):
    
   # posts = serializers.PrimaryKeyRelatedField(many=True, queryset=User_Post.objects.all())
    
    class Meta:
        model = User
        fields = '__all__'