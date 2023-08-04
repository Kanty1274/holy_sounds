from django.urls import path
from . import views

app_name = 'band'

urlpatterns = [
    path('', views.band_page, name='band'),
    path('details/', views.details_page, name='details'),
    path('song-list/', views.song_list_page, name='song_list'),
]