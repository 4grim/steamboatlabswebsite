from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
	url(r'^$', views.blog_index, name='blog_index'),
	url(r'^(?P<entry_id>\d+)/$', views.entry, name='entry'),
	url(r'^categories/(?P<category_id>\d+)/$', views.index_of_category, name='index_of_category'),
	url(r'^authors/(?P<author_id>\d+)/$', views.index_of_author, name='index_of_author'),
	url(r'^tags/(?P<slug>\w+)/$', views.index_of_tag, name='index_of_tag'),
	)