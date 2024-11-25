from django import forms
from .models import cancion

class libroform(forms.ModelForm):
    class Meta:
        model = cancion
        fields = '__all__'
