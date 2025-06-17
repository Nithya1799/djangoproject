from django.db import models

class Movies(models.Model):
    name=models.CharField(max_length=100)
    director_name=models.CharField(max_length=100)
    description=models.TextField()
    language=models.CharField(max_length=100)
    Year= models.IntegerField()
    image = models.ImageField(upload_to="movies")

