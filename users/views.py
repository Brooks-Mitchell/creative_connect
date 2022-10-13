from django.shortcuts import render

# Create your views here.

# TEMPORARY, WILL NOT BE ON USERS LATER
def front(request):
    context = {}
    return render(request, 'index.html', context)