from django.db import models

class ProjectImage(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='projects')

	def __unicode__(self):
		return self.title


class Client(models.Model):
	company_name = models.CharField(max_length=200, default='')
	company_logo = models.ImageField(upload_to='projects', blank=True, default='')
	company_website = models.URLField(blank=True, default='')
	testimonial = models.TextField()

	def __unicode__(self):
		return self.company_name


class Project(models.Model):
	title = models.CharField(max_length=200)
	project_start = models.DateField()
	project_end = models.DateField()
	description = models.TextField()
	technologies = models.TextField()
	accomplishments = models.TextField()
	feature_project = models.BooleanField()
	images = models.ManyToManyField(ProjectImage, blank=True)
	client = models.ForeignKey(Client)

	def __unicode__(self):
		return self.title



