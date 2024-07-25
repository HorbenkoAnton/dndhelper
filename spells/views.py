from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy
from .models import Spell
from .forms import SpellForm

class SpellListView(ListView):
    model = Spell
    template_name = 'spell_list.html'
    context_object_name = 'spells'

class SpellCreateView(CreateView):
    model = Spell
    form_class = SpellForm
    template_name = 'spell_create.html'
    success_url = reverse_lazy('spells:spell_list')

class SpellUpdateView(UpdateView):
    model = Spell
    form_class = SpellForm
    template_name = 'spell_update.html'
    success_url = reverse_lazy('spells:spell_list')

class SpellDeleteView(DeleteView):
    model = Spell
    success_url = reverse_lazy('spells:spell_list')
