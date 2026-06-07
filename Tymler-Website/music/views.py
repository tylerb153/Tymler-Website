from django.shortcuts import render

# Create your views here.
def music(request):

    # Get the songs
    # Pass that to context

    context = {}
    return render(request, 'music.html', context)