from django.contrib import admin

from blog.models import Category, Author, EntryImage, EntryFile, Entry


class EntryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	date_hierarchy = 'post_date'


class EntryImageAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

class EntryFileAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("title",)}


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(EntryImage, EntryImageAdmin)
admin.site.register(EntryFile, EntryFileAdmin)
admin.site.register(Entry, EntryAdmin)