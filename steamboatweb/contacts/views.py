from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from contacts.models import Contact
from contacts.forms import ContactForm

def contact_index(request):
	#uneccessary
	contacts = Contact.objects.all()
	context = {'contacts': contacts}

	return render(request, 'contacts/contact_index.html', context)

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			#send mail to steamboatlabs
			send_mail(
				cd['subject'],
				cd['message'],
				cd['email'],
				#emails that will recieve correspondence from contact form
				['amber@steamboatlabs.com'],
			)
			message = form.save()
			message
			message_id = message.id
			url = '/contacts/contact/thanks/' + str(message_id)
			return HttpResponseRedirect(url)
	else:
		form = ContactForm()
		return render(request, 'contacts/contact_form.html', {'form': form})	

def contact_submitted(request, message_id):
	#takes a primary key to fetch the ontact obj and pass to the template
	message = get_object_or_404(Contact, pk=message_id)
	confirmation = message.id
	context = {'confirmation': confirmation, 'message': message}

	#send mail to sender
	send_mail(
		message.subject,
		message.message,
		message.email,
		[message.email],
		)

	return render(request, 'contacts/contact_submitted.html', context)






