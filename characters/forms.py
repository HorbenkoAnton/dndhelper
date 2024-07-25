from django import forms
from .models import BasicInfo, CharacterSheet,Stats


class CharacterSheetForm(forms.ModelForm):
    class Meta:
        model = CharacterSheet
        fields = []

class CharacterSheetUpdateForm(forms.ModelForm):
    class Meta:
        model = CharacterSheet
        fields = []

class BasicInfoForm(forms.ModelForm):
    class Meta:
        model = BasicInfo
        fields = ['name','race','class_type','level']

class BasicInfoUpdateForm(forms.ModelForm):
    class Meta:
        model = BasicInfo
        fields = ['name', 'race', 'class_type', 'level']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = 'readonly'
        self.fields['race'].widget.attrs['readonly'] = 'readonly'
        self.fields['class_type'].widget.attrs['readonly'] = 'readonly'


class StatsForm(forms.ModelForm):
    class Meta:
        model = Stats
        fields = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']






