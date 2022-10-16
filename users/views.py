from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.

# TEMPORARY, WILL NOT BE ON USERS LATER
def front(request):
    context = {}
    return render(request, 'index.html', context)

def register(request):
    pass