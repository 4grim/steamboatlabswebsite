from django.contrib import admin

from blog.models import Category, Author, EntryImage, EntryFile, Entry


class EntryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	date_hierarchy = 'post_date'


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(EntryImage)
admin.site.register(EntryFile)
admin.site.register(Entry, EntryAdmin)