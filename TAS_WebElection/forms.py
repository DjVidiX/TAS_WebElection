# -*- coding: UTF-8 -*-

__author__ = 'marek'

from django import forms


class ContactForm(forms.Form):
    tytul = forms.CharField()
    email = forms.EmailField(required=False)
    wiadomosc = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['wiadomosc']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError(u"Za mało słów")
        return message

