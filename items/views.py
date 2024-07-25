from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy
from .models import Item
from .forms import ItemForm

class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'
    context_object_name = 'items'

class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_create.html'
    success_url = reverse_lazy('items:item_list')

class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_update.html'
    success_url = reverse_lazy('items:item_list')

class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('items:item_list')
