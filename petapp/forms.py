from django import forms

class PetForm(forms.Form):
    breed = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Breed'}))
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))