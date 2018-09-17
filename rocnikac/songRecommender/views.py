from django.shortcuts import render
from songRecommender.models import Song, List, Song_in_List, Played_Song, Distance_to_User, Distance_to_List, Distance

# Create your views here.

def index(request):
    songs = Song.objects.all()

    context = {
        'songs': songs
    }

    return render(request, 'index.html', context=context)