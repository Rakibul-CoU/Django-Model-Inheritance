from django.contrib import admin

# Register your models here.
from .models import Publication, Book, Magazine

class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "publisher")

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "publisher", "author", "price")

class MagazineAdmin(admin.ModelAdmin):
    list_display = ("title", "publisher","issue_number")


admin.site.register(Publication, PublicationAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Magazine, MagazineAdmin)