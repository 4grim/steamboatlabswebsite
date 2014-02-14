from django.conf.urls import patterns, url
from contact import views

urlpatterns = patterns('',
	url(r'^contact_index/$', views.contact_index, name='contact_index'),
	url(r'^$', views.contact, name='contact'),
	url(r'^thanks/(?P<message_id>\d+)/$', views.contact_submitted, name='contact_submitted'),
	)