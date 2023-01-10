from django import forms

class AnimalForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.FloatField()
    breed = forms.CharField(max_length=100)
    exotic = forms.BooleanField()
    baby = forms.BooleanField()
