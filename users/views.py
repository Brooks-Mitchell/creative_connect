from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from users.serializers import UserSerializer


# Create your views here.

# TEMPORARY FRONT PAGE
def front(request):
    context = {}
    return render(request, 'index.html', context)

def register(request):
    pass
# end temp front

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(APIView):
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)