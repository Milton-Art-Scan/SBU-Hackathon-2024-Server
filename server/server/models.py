from django.db import models
from django.contrib.postgres.fields import ArrayField


class Art(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    year = models.IntegerField()
    tags = ArrayField(models.CharField(max_length=100), default=list, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='art_images')


    def __str__(self):
        return self.title
