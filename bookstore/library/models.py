from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    cover_page = models.CharField(max_length=255)

    def __str__(self):
        return self.title