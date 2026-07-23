from django.db import models
from django.dispatch import receiver
from django_resized import ResizedImageField
import os

# Create your models here.
class Book(models.Model):
    title = models.CharField()
    author = models.CharField()
    coverArt = ResizedImageField(force_format="WEBP", crop=['middle', 'center'], upload_to='books/')
    description = models.TextField(null=True)
    releaseDate = models.DateField()
    featured = models.BooleanField()

    def __str__(self):
        return self.title

class Link(models.Model):
    service = models.CharField(max_length=255)
    url = models.TextField()
    embed = models.BooleanField(default=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="links")

    def __str__(self):
        return f"{self.song.title} - {self.service}"

@receiver(models.signals.post_delete, sender=Book)
def deleteImageFile(sender, instance, **kwargs):
    if instance.coverArt and os.path.isfile(instance.coverArt.path):
        os.remove(instance.coverArt.path)