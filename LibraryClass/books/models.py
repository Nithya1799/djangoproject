from django.db import models

# Create your models here.


#Model Definition(database Schema)
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    price=models.IntegerField()
    language=models.CharField(max_length=100)
    pages=models.IntegerField()
    image=models.ImageField(upload_to="books")
