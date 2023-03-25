from django import forms


class ContactForm(forms.Form):
    lastname = forms.CharField
    firstname = forms.CharField
    surname = forms.CharField
    company = forms.CharField
    number = forms.CharField
    email = forms.EmailField
