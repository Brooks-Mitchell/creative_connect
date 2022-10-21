from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import User_Profile
from rest_framework.validators import UniqueValidator

from user_posts.models import User_Post

class UserSerializer(serializers.ModelSerializer):
    
    #posts = serializers.PrimaryKeyRelatedField(many=True, queryset=User_Post.objects.all())

    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
             
        user.set_password(validated_data['password'])
        user.save()
        return user

        



class UserProfileSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User_Profile
        fields = '__all__'