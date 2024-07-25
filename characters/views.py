from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CharacterSheet
from .forms import CharacterSheetForm,BasicInfoForm,CharacterSheetUpdateForm,BasicInfoUpdateForm,StatsForm
from django.shortcuts import render, redirect
from django.views.generic.edit import FormMixin


class CharacterSheetFormMixin(FormMixin):
    basic_info_form_class = None
    stats_form_class = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['basic_info_form'] = self.basic_info_form_class(self.request.POST, instance=self.get_basic_info_instance())
            context['stats_form'] = self.stats_form_class(self.request.POST, instance=self.get_stats_instance())
        else:
            context['basic_info_form'] = self.basic_info_form_class(instance=self.get_basic_info_instance())
            context['stats_form'] = self.stats_form_class(instance=self.get_stats_instance())
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        basic_info_form = context['basic_info_form']
        stats_form = context['stats_form']
        
        if form.is_valid() and basic_info_form.is_valid() and stats_form.is_valid():
            # Save BasicInfo
            basic_info = basic_info_form.save(commit=False)
            basic_info.user = self.request.user
            basic_info.save()

            # Save Stats
            stats = stats_form.save()

            # Save CharacterSheet
            self.object = form.save(commit=False)
            self.object.basic_info = basic_info
            self.object.stats = stats
            self.object.save()
            
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
    
    def get_basic_info_instance(self):
        # Return the instance of BasicInfo if it exists or None
        if hasattr(self, 'object') and self.object.basic_info:
            return self.object.basic_info
        return None

    def get_stats_instance(self):
        # Return the instance of Stats if it exists or None
        if hasattr(self, 'object') and self.object.stats:
            return self.object.stats
        return None

class CharacterSheetCreateView(CharacterSheetFormMixin, CreateView):
    model = CharacterSheet
    form_class = CharacterSheetForm
    template_name = 'character_sheet/character_sheet_create.html'
    success_url = reverse_lazy('characters:character_sheet_list')
    
    basic_info_form_class = BasicInfoForm
    stats_form_class = StatsForm

class CharacterSheetUpdateView(CharacterSheetFormMixin, UpdateView):
    model = CharacterSheet
    form_class = CharacterSheetForm
    template_name = 'character_sheet/character_sheet_update.html'
    context_object_name = 'character_sheet'
    success_url = reverse_lazy('characters:character_sheet_list')
    
    basic_info_form_class = BasicInfoUpdateForm
    stats_form_class = StatsForm


class CharacterSheetListView(ListView):
    model = CharacterSheet
    template_name = 'character_sheet_list.html'
    context_object_name = 'character_sheets'

class CharacterSheetDetailView(DetailView):
    model = CharacterSheet
    template_name = 'character_sheet_detail.html'
    context_object_name = 'character_sheet'

class CharacterSheetDeleteView(DeleteView):
    model = CharacterSheet
    template_name = 'character_sheet_confirm_delete.html'
    success_url = reverse_lazy('characters:character_sheet_list')
