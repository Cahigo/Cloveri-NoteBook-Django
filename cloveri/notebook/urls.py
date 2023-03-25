from django.urls import path
from .views import ContactsList, CompaniesList, contacts_post

urlpatterns = [
    path('contacts/', ContactsList.as_view()),
    path('companies/', CompaniesList.as_view()),
    path('add_contact/', contacts_post)
]