from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Imię i nazwisko", max_length=50)
    email = forms.CharField(label="Adres email", max_length=50)
    subject = forms.CharField(label="Temat wiadomości", max_length=50)
    body = forms.CharField(widget=forms.Textarea, label="Treść wiadomości")
