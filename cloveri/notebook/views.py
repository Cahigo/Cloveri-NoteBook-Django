from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Contact, Company
from .forms import ContactForm


class ContactsList(ListView):
    model = Contact
    # ordering = 'lastname'
    template_name = 'contacts.html'
    context_object_name = 'contacts'


def contacts_post(request):
    lastname = ""
    firstname = ""
    surname = ""
    company = ""
    number = ""
    email = ""
    form = ContactForm(request.POST or None)
    if form.is_valid():
        lastname = form.cleaned_data.get("lastname")
        firstname = form.cleaned_data.get("firstname")
        surname = form.cleaned_data.get("surname")
        company = form.cleaned_data.get("company")
        number = form.cleaned_data.get("number")
        email = form.cleaned_data.get("email")
    context = {
        'form': form,
        'firstname': firstname, 'lastname': lastname, 'surname': surname,
        'company': company, 'number': number, 'email': email,
    }
    return render(request, 'templates/add_contact.html', context)


class CompaniesList(ListView):
    model = Company
    # ordering = 'name'
    template_name = 'companies.html'
    context_object_name = 'companies'
