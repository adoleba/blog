from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template

from contact.forms import ContactForm
from contact.models import ContactPage


def contact(request):
    contact = get_object_or_404(ContactPage, pk=1)

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            body = request.POST.get('body', '')

            template = get_template('contact/email.html')
            context = {
                'name': name,
                'email': email,
                'subject': subject,
                'body': body
            }
            content = template.render(context)

            email = EmailMessage(
                "Wiadomość z formularza kontaktowego",
                content,
                "blog" + '',
                ['django.ania@gmail.com'],
                headers={'Reply-To': email}
            )
            email.content_subtype = 'html'
            email.send()

            return redirect('contact:contact_thank_you')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'contact': contact, 'form': form})


def contact_thank_you(request):
    return render(request, 'contact/contact_thank_you.html')
