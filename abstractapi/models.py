from django.db import models

class CommonFields(models.Model):
    common_field = models.CharField(max_length=100)
    
    class Meta:
        abstract = True

class MyModel(CommonFields):
    additional_field = models.CharField(max_length=100)
