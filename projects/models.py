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
	testimonial = models.TextField(blank=True)

	def __unicode__(self):
		return self.company_name


class Project(models.Model):
	title = models.CharField(max_length=200)
	months_in_year = (
		('January', 'January'),
		('February', 'February'),
		('March', 'March'),
		('April', 'April'),
		('May', 'May'),
		('June', 'June'),
		('July', 'July'),
		('August', 'August'),
		('September', 'September'),
		('October', 'October'),
		('November', 'November'),
		('December', 'December'),
	)
	project_start_month = models.CharField(max_length=9, choices=months_in_year, default='January')
	project_start_year = models.PositiveIntegerField(max_length=4)
	project_end_month = models.CharField(max_length=9, choices=months_in_year, default='January')
	project_end_year = models.PositiveIntegerField(max_length=4)
	description = models.TextField()
	technologies = models.TextField(blank=True)
	accomplishments = models.TextField()
	feature_project = models.BooleanField()
	images = models.ManyToManyField(ProjectImage, blank=True)
	client = models.ForeignKey(Client)

	def __unicode__(self):
		return self.title


class MediaLink(models.Model):
	publication = models.CharField(max_length=200)
	link = models.URLField()
	quote = models.TextField(blank=True)
	project = models.ForeignKey(Project, null=True)

	def __unicode__(self):
		return self.publication

