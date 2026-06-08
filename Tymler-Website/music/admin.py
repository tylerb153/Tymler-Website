from django.contrib import admin
from .models import Song, Link

# Register your models here.

@admin.register(Song)
class AdminSong(admin.ModelAdmin):
    list_display = ['title', 'artist', 'genre', 'releaseDate', 'featured']
    list_filter = ['featured', 'genre', 'artist']
    search_fields = ['title', 'artist', 'genre']

@admin.register(Link)
class AdminLink(admin.ModelAdmin):
    list_display = ['service', 'song']
    list_filter = ['service', 'song']
    search_fields = ['service', 'song']