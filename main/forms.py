from django import forms

class SongForm(forms.Form):
    url = forms.CharField(label='url', max_length=200)
    location = forms.CharField(label='location', max_length=200,initial=".")