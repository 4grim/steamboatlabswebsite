from django.db import models


class Tag(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name


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
	author = models. ForeignKey('Author')
	post_date = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(max_length=50)
	tags = models.ManyToManyField(Tag, blank=True)
	categories = models.ManyToManyField(Category, blank=True)
	images = models.ManyToManyField(EntryImage, blank=True)
	files = models.ManyToManyField(EntryFile, blank=True)

	def __unicode__(self):
		return self.title

	# def all_tags(self):
	# 	entry_tags = filter(Entry, self.tags)
	# 	return entry_tags

	# on monel put a method called all tags and retun 
	# self.tags.filter to be an interable of all the tags 
	# the thing has



