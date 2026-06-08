from django.db import models
from django.dispatch import receiver
from django.conf import settings
from django_resized import ResizedImageField
import os

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=100)
    coverArt = ResizedImageField(force_format="WEBP", crop=['middle', 'center'], upload_to='music/')
    description = models.TextField(null=True)
    genre = models.CharField(max_length=100, blank=True)
    releaseDate = models.DateField()
    featured = models.BooleanField()

class Link(models.Model):
    service = models.CharField(max_length=255)
    url = models.TextField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="links")


@receiver(models.signals.post_delete, sender=Song)
def deleteImageFile(sender, instance, **kwargs):
    if instance.coverArt and os.path.isfile(instance.coverArt.path):
        os.remove(instance.coverArt.path)