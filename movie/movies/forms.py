from django import forms
from .models import Film, Actor

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['film_name']