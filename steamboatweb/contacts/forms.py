from django import forms
from django.forms import ModelForm
from contacts.models import Contact

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		exclude = ['date_created']

	