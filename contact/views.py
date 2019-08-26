from django.shortcuts import render, get_object_or_404

from contact.forms import ContactForm
from contact.models import ContactPage


def contact(request):
    contact = get_object_or_404(ContactPage, pk=1)
    form = ContactForm()
    return render(request, 'contact/contact.html', {'contact': contact, 'form': form})
