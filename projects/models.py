from django.db import models

class ProjectImage(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='projects')

	def __unicode__(self):
		return self.title


class MediaLink(models.Model):
	publication = models.CharField(max_length=200)
	link = models.URLField()
	quote = models.TextField(blank=True)

	def __unicode__(self):
		return self.publication


class Client(models.Model):
	company_name = models.CharField(max_length=200, default='')
	company_logo = models.ImageField(upload_to='projects', blank=True, default='')
	company_website = models.URLField(blank=True, default='')
	testimonial = models.TextField(blank=True)

	def __unicode__(self):
		return self.company_name


class Project(models.Model):
	title = models.CharField(max_length=200)
	project_start = models.DateField()
	project_end = models.DateField()
	description = models.TextField()
	technologies = models.TextField(blank=True)
	accomplishments = models.TextField()
	feature_project = models.BooleanField()
	images = models.ManyToManyField(ProjectImage, blank=True)
	client = models.ForeignKey(Client)
	media_links = models.ManyToManyField(MediaLink, blank=True)

	def __unicode__(self):
		return self.title



