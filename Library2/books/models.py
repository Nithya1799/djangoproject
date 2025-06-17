from django.db import models


# model definition(database schema)
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.FloatField()
    pages = models.IntegerField()
    language = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books')
