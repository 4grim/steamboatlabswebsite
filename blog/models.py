import re
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
	slug = models.SlugField(unique=True, default='default')
	image = models.ImageField(upload_to='blog', blank=True)
	feature_image = models.BooleanField(default=False)

	def __unicode__(self):
		return self.title


class EntryFile(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	slug = models.SlugField(unique=True, default='default')
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
		regex = r"\[img:([a-zA-Z0-9-_]+)\]"
		current_text = self.text
		search = re.search(regex, current_text)

		while search:
			slug = current_text[search.start(1):search.end(1)]
			to_be_replaced = current_text[search.start():search.end()]
			image = EntryImage.objects.get(slug=slug)
			markdown_tag = '![Alt text](' + str(image.image.url) +')'
			replacement = current_text.replace(to_be_replaced, markdown_tag)
			current_text = replacement
			search = re.search(regex, current_text)
		return markdown(current_text, extensions=['codehilite(linenums=True)'])

	def __unicode__(self):
		return self.title






