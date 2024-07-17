from django import forms
from .models import Item,Spell,CharacterSheet

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class SpellForm(forms.ModelForm):
    class Meta:
        model = Spell
        fields = '__all__'


class CharacterSheetForm(forms.ModelForm):
    class Meta:
        model = CharacterSheet
        fields = '__all__'