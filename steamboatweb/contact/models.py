from django.db import models

class Contact(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	date_created = models.DateTimeField(auto_now_add=True)
	subject = models.CharField(max_length=200)
	message = models.TextField()

	def __unicode__(self):
		return self.subject 

