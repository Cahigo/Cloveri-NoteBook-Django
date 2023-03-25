from django.db import models


class Contact(models.Model):  # Inspired by Google Contacts
    lastname = models.CharField
    firstname = models.CharField
    surname = models.CharField
    company = models.CharField
    number = models.CharField
    email = models.EmailField


class Company(models.Model):
    name = models.CharField
    address = models.CharField
    number = models.CharField
    email = models.EmailField
    site = models.CharField


class ContactCompanyLinks(models.Model):
    contact = models.ManyToManyField(Contact)
    company = models.ManyToManyField(Company)
