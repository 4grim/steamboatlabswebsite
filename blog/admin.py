from django.contrib import admin

from blog.models import Tag, Category, Author, EntryImage, EntryFile, Entry

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(EntryImage)
admin.site.register(EntryFile)
admin.site.register(Entry)

class EntryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}