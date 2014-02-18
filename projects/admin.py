from django.contrib import admin
from projects.models import Project, ProjectImage, Client, MediaLinks


admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(Client)
admin.site.register(MediaLinks)

