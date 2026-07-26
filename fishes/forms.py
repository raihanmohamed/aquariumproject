from django import forms
from .models import Fish


class FishForm(forms.ModelForm):
    class Meta:
        model = Fish
        fields = ['fish_name', 'species', 'tank_number', 'price']
        widgets = {
            'fish_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Goldfish'}),
            'species': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Carassius auratus'}),
            'tank_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. T-01'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 250'}),
        }
