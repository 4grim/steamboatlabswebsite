from django.contrib import admin

from about.models import TeamMember, Link, Media

admin.site.register(TeamMember)
admin.site.register(Link)
admin.site.register(Media)