from django.shortcuts import render, redirect
from .models import Stuff

# Create your views here.
def index(request):
    items = Stuff.objects.all()
    return render(request, 'index.html', {'items': items})

