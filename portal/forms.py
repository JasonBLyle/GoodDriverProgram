from django import forms

class SearchBar(forms.ModelForm):
    search = forms.CharField(label = 'give me a search you absolute goon')