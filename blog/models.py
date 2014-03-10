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
	feature_image = models.BooleanField(default=False)

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
	slug = models.SlugField(unique=True)
	categories = models.ManyToManyField(Category, blank=True)
	tags = TaggableManager()
	images = models.ManyToManyField(EntryImage, blank=True)
	files = models.ManyToManyField(EntryFile, blank=True)

	def next(self):
		entries = Entry.objects.order_by('post_date').filter(post_date__gt=self.post_date)
		if entries.count():
			return entries[0]

	def previous(self):
		entries = Entry.objects.order_by('-post_date').filter(post_date__lt=self.post_date)
		if entries.count():
			return entries[0]

	@property
	def text_to_html(self):
		return markdown(self.text, extensions=['codehilite(linenums=True)'])

	def __unicode__(self):
		return self.title






