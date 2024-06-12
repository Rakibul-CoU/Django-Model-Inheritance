from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.CharField(max_length=50)

class Book(Publication):
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class Magazine(Publication):
    issue_number = models.IntegerField()