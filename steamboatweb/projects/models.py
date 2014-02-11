from django.db import models

class ProjectImage(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='projects')

	def __unicode__(self):
		return self.title


class Project(models.Model):
	title = models.CharField(max_length=200)
	project_start = models.DateField()
	project_end = models.DateField()
	description = models.TextField()
	company_name = models.CharField(max_length=200)
	company_logo = models.ImageField(upload_to='projects', blank=True)
	company_website = models.URLField(blank=True)
	technologies = models.TextField()
	accomplishments = models.TextField()
	feature_project = models.BooleanField()
	images = models.ManyToManyField(ProjectImage, blank=True)

	def __unicode__(self):
		return self.title

