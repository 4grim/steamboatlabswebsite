from collections import OrderedDict
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Category, Author, EntryImage, EntryFile, Entry
from taggit.models import Tag

def get_context_data():
	entries = Entry.objects.all().order_by('-post_date')
	categories = Category.objects.all()
	authors = Author.objects.all()
	tags = Tag.objects.all()
	context = {
		'entries': entries, 
		'categories': categories, 
		'authors': authors, 
		'tags': tags,
	}
	return context
		
# main blog index
def blog_index(request):
	context = get_context_data()
	entry_list = context['entries']
	paginator = Paginator(entry_list, 3)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(pagintor.num_pages)
	context['posts'] = posts	
	return render(request, 'blog/blog_index.html', context)

# entry post
def entry(request, slug):
	context = get_context_data()
	entry = get_object_or_404(Entry, slug=slug)
	featured_image = entry.images.filter(feature_image=True)
	entry_files = entry.files
	entry_list = context['entries']
	paginator = Paginator(entry_list, 1)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(pagintor.num_pages)

	context_add = {
		'entry': entry, 
		'entry_files': entry_files, 
		'posts': posts,
		'featured_image': featured_image,
	}
	context.update(context_add)
	return render(request, 'blog/entry.html', context)

# all blogs within a category
def index_of_category(request, category_id):
	context = get_context_data()
	related_posts = Entry.objects.filter(categories__id=category_id)
	entry = Entry.objects.filter
	paginator = Paginator(related_posts, 3)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(pagintor.num_pages)
	context_add = {
		'related_posts': related_posts, 
		'posts': posts,
	}
	context.update(context_add)
	return render(request, 'blog/category_page.html', context)

# all blogs by an author
def index_of_author(request, author_id):
	context = get_context_data()
	related_posts = Entry.objects.filter(author__id=author_id)
	paginator = Paginator(related_posts, 3)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(pagintor.num_pages)
	context_add = {'related_posts': related_posts, 'posts': posts}
	context.update(context_add)
	return render(request, 'blog/author_page.html', context)

# all blogs with a specific tag
def index_of_tag(request, slug):
	context = get_context_data()
	related_posts = Entry.objects.filter(tags__name=slug)
	paginator = Paginator(related_posts, 3)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(pagintor.num_pages)
	context_add = {'related_posts': related_posts, 'posts': posts}
	context.update(context_add)
	return render(request, 'blog/tag_page.html', context)

# all entries
def archive(request):
	context = get_context_data()
	post_dates = []
	archive_dict = OrderedDict({})
	for entry in context['entries']:
		entry_date = entry.post_date.strftime('%b %Y')
		if entry_date not in post_dates:
			post_dates.append(entry_date)
	for entry in context['entries']:
		for date in post_dates:
			if entry.post_date.strftime('%b %Y') == date:
				if date in archive_dict: 
					archive_dict[date].append(entry)
				else:
					archive_dict[date] = [entry]
	context_add = {'post_dates': post_dates, 'archive_dict': archive_dict}
	context.update(context_add)
	return render(request, 'blog/archive.html', context)


