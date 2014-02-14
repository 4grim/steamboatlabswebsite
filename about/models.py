from django.db import models


class TeamMember(models.Model):
	name = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	photo = models.ImageField(upload_to='about')
	bio = models.TextField()

	def __unicode__(self):
		return self.name

	def links(self):
		return Link.objects.filter(teammember=self)


class Link(models.Model):
	title = models.CharField(max_length=200)
	url = models.URLField()
	icon = models.ImageField(upload_to='about', default='True')
	teammember = models.ForeignKey(TeamMember)

	def __unicode__(self):
		return self.title


class Media(models.Model):
	title = models.CharField(max_length=200)
	publication = models.CharField(max_length=200)
	url = models.URLField()
	quote = models.TextField()

	def __unicode__(self):
		return self.title