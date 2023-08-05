from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Song

def band_page(request):
    """
    Render the band page.

    This function renders the 'band.html' template and returns it as a response.
    The 'band.html' template is used to display information about a particular band.

    :param request (HttpRequest): The HTTP request object sent by the client.

    :return: The rendered response containing the 'band.html' template.
    
    :rtype: HttpResponse
    
    """
    return render(request, 'bands/band.html')


def details_page(request):
    """
    Render the details page.

    This function renders the 'details.html' template and returns it as a response.
    The 'details.html' template is used to display specific details about a band or an event.

    Parameters:
        request (HttpRequest): The HTTP request object sent by the client.

    Returns:
        HttpResponse: The rendered response containing the 'details.html' template.
    """
    return render(request, 'bands/details.html')


@login_required(login_url='/user_auth/')
def song_list_page(request):
    """
    Render the song list page.

    This function requires the user to be logged in to access the page, and if not logged in,
    it will redirect the user to the '/user_auth/' URL for authentication.

    The function retrieves all the songs from the database using the Song model and passes
    them to the 'song_list.html' template for rendering.

    
    :param request (HttpRequest): The HTTP request object sent by the client.

    :return: The rendered response containing the 'song_list.html' template with the 'songs' context variable.
    
    :rtype: HttpResponse
    """
    songs = Song.objects.all()
    return render(request, 'bands/song_list.html', {'songs': songs})







