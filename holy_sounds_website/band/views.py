from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Song

def band_page(request):
    return render(request, 'bands/band.html')


def details_page(request):
    return render(request, 'bands/details.html')

@login_required(login_url='/user_auth/')
def song_list_page(request):
    songs = Song.objects.all()
    return render(request, 'bands/song_list.html', {'songs': songs})


