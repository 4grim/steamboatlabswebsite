from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
	url(r'^$', views.blog_index, name='blog_index'),
	url(r'^archive/$', views.archive, name='archive'),
	url(r'^categories/(?P<category_id>\d+)/$', views.index_of_category, name='index_of_category'),
	url(r'^authors/(?P<author_id>\d+)/$', views.index_of_author, name='index_of_author'),
	url(r'^tags/(?P<slug>[a-zA-Z0-9-_]+)/$', views.index_of_tag, name='index_of_tag'),
	url(r'^(?P<slug>[a-zA-Z0-9-_]+)/$', views.entry, name='entry'),
	)