from django import forms
from .models import Spell

class SpellForm(forms.ModelForm):
    class Meta:
        model = Spell
        fields = ['name', 'description', 'level']
