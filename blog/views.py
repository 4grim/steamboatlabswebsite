from django.shortcuts import render, get_object_or_404
from blog.models import Tag, Category, Author, EntryImage, EntryFile, Entry

def blog_index(request):
	entries = Entry.objects.all()
	categories = Category.objects.all()
	tags = Tag.objects.all()
	authors = Author.objects.all()

	context = {'entries': entries, 'tags': tags, 'categories': categories, 'authors': authors,}
	return render(request, 'blog/blog_index.html', context)

def entry(request, entry_id):
	entry = get_object_or_404(Entry, pk=entry_id)
	entry_images = entry.images
	entry_files = entry.files
	context = {'entry': entry, 'entry_images': entry_images, 'entry_files': entry_files}

	return render(request, 'blog/entry.html', context)

# all categories
def category_index(request):
	categories = Category.objects.all()
	context = {'categories': categories}
	return render(request, 'blog/category_index.html', context)

# all blogs within a category
def index_of_category(request, category_id):
	return render(request, 'blog/category_page.html', context)

# all authors
def author_index(request):
	authors = Author.objects.all()
	context = {'authors': authors}
	return render(request, 'blog/author_index.html', context)

# all blogs by an author
def index_of_author(request, author_id):
	return render(request, 'blog/author_page.html', context)

# all tags
def tag_index(request):
	tags = Tag.objects.all()
	context = {'tags': tags}
	return render(request, 'blog/tag_index.html', context)

# all blogs with a specific tag
def index_of_tag(request, tag_id):
	return render(request, 'blog/tag_page.html', context)

