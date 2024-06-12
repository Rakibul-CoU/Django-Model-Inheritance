from django.contrib import admin

# Register your models here.

from .models import OriginalModel, ProxyModel

class OriginalModelAdmin(admin.ModelAdmin):
    list_display = ["field"]

admin.site.register(OriginalModel, OriginalModelAdmin)

class ProxyModelAdmin(admin.ModelAdmin):
    list_display = ["field"]

admin.site.register(ProxyModel, ProxyModelAdmin)

