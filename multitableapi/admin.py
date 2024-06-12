from django.contrib import admin

# Register your models here.

from .models import ParentModel, ChildModel

class ParentModelAdmin(admin.ModelAdmin):
    list_display = ["common_field"]

admin.site.register(ParentModel, ParentModelAdmin)

class ChildModelAdmin(admin.ModelAdmin):
    list_display = ["common_field", "additional_field"]

admin.site.register(ChildModel, ChildModelAdmin)
