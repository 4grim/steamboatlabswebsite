from django.db import models
from taggit.managers import TaggableManager
from markdown import markdown


class Category(models.Model):
	title = models.CharField(max_length=50)

	def __unicode__(self):
		return self.title


class Author(models.Model):
	name = models.TextField(max_length=200)

	def __unicode__(self):
		return self.name


class EntryImage(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='blog', blank=True)

	def __unicode__(self):
		return self.title


class EntryFile(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	entry_file = models.FileField(upload_to='blog', blank=True)

	def __unicode__(self):
		return self.title


class Entry(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	author = models.ForeignKey('Author')
	post_date = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField()
	categories = models.ManyToManyField(Category, blank=True)
	tags = TaggableManager()
	images = models.ManyToManyField(EntryImage, blank=True)
	files = models.ManyToManyField(EntryFile, blank=True)

	@property
	def text_to_html(self):
		return markdown(self.text, extensions=['codehilite(linenums=True)'])

	def __unicode__(self):
		return self.title






