__author__ = 'marek'

from django import forms


class ContactForm(forms.Form):
    tytul = forms.CharField()
    email = forms.EmailField(required=False)
    wiadomosc = forms.CharField(widget=forms.Textarea)
