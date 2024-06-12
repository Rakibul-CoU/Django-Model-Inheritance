from django.db import models

# Create your models here.

class OriginalModel(models.Model):
    field = models.CharField(max_length=100)

class ProxyModel(OriginalModel):
    class Meta:
        proxy = True
