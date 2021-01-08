from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Stuff
from .forms import ItemForm

# Create your views here.
def index(request):
    items = Stuff.objects.all()
    item_form = ItemForm()
    total_quant = 0
    for item in items:
        total_quant += item.quantity
    return render(request, 'index.html', {
        'items': items, 
        'item_form': item_form,
        'total_quant': total_quant})

def add_item(request):
  print('working')
  form = ItemForm(request.POST)
  if form.is_valid():
    new_item = form.save(commit=False)
    new_item.save()
  return redirect('index')

def delete_item(request, item_id):
  Stuff.objects.get(id=item_id).delete()
  return redirect('/')