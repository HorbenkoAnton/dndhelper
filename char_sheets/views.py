from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Item, Spell,CharacterSheet
from .forms import ItemForm, SpellForm ,CharacterSheetForm
from django.views.generic import ListView,DetailView
from django.urls import reverse_lazy
#ITEM VIEWS
class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_create_form.html'
    success_url = reverse_lazy('item-list')

class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'
    context_object_name = 'items'

#SPELL VIEWS
class SpellCreateView(CreateView):
    model = Spell
    form_class = SpellForm
    template_name = 'spell_create_form.html'
    success_url = reverse_lazy('spell-list')


class SpellListView(ListView):
    model = Spell
    template_name = 'spell_list.html'
    context_object_name = 'spells'

#CHARECTER VIEWS
class CharacterSheetCreateView(CreateView):
    model = CharacterSheet
    form_class = CharacterSheetForm
    template_name = 'character_sheet_creation.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CharacterSheetDetailView(DetailView):
    model = CharacterSheet
    template_name = 'character_sheet_detail.html'
    context_object_name = 'character_sheet'

class CharacterSheetListView(ListView):
    model = CharacterSheet
    template_name = 'character_sheet_list.html'
    context_object_name = 'character_sheets'