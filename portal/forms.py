from django import forms

class SearchBar(forms.ModelForm):
    search = forms.CharField(label = 'search')