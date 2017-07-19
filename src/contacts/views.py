from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ContactsView(TemplateView):
    template_name = 'contacts/contacts.html'
