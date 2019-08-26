from django.urls import path

from contact.views import contact, contact_thank_you

app_name = 'contact'

urlpatterns = [
    path('', contact, name='contact'),
    path('thank_you', contact_thank_you, name='contact_thank_you'),
]
