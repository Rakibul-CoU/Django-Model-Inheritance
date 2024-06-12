from django.db import models

class ParentModel(models.Model):
    common_field = models.CharField(max_length=100)

class ChildModel(ParentModel):
    additional_field = models.CharField(max_length=100)

