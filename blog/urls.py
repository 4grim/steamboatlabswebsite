from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
	url(r'^$', views.blog_index, name='blog_index'),
	url(r'(?P<entry_id>\d+)/$', views.entry, name='entry'),
	url(r'categories/$', views.category_index, name='category_index'),
	url(r'categories/(?P<category_id>\d+)/$', views.index_of_category, name='index_of_category'),
	url(r'authors/$', views.author_index, name='author_index'),
	url(r'authors/(?P<author_id>\d+)/$', views.index_of_author, name='index_of_author'),
	url(r'tags/$', views.tag_index, name='tag_index'),
	url(r'tags/(?P<tag_id>\d+)/$', views. index_of_tag, name='index_of_tag'),
	)