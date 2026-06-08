from django.shortcuts import render
from .models import Song

# Create your views here.
def music(request):

    # Get the songs
    # Pass that to context
    songs = Song.objects.all()
    featuredSong = songs.filter(featured=True).first()
    

    context = {'songs': songs, 'featuredSong': featuredSong}
    return render(request, 'music.html', context)