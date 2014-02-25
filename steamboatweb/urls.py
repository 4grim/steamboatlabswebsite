from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from steamboatweb import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'steamboatweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('projects.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
