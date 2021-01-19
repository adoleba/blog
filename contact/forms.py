from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Firstname and lastname", max_length=50)
    email = forms.CharField(label="Email", max_length=50)
    subject = forms.CharField(label="Subject", max_length=50)
    body = forms.CharField(widget=forms.Textarea, label="Message")
