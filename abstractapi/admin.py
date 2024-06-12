from django.contrib import admin

from .models import MyModel

class MyModelAdmin(admin.ModelAdmin):
    list_display = ["common_field", "additional_field"]

admin.site.register(MyModel, MyModelAdmin)

