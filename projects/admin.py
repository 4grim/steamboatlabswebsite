from django.contrib import admin
from projects.models import Project, ProjectImage, Client


admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(Client)

