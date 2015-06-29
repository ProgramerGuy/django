from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from rest_framework import viewsets
from .serializer import ArtistSerializer

from .models import Artist

# detalle de un artista
class ArtistDetailView(DetailView):
    model = Artist
    context_object_name = 'fav_artist'
    template_name = 'artists.html'

class ArtistListView(ListView):
    model = Artist
    context_object_name = 'artists'
    template_name = 'artists.html'


class ArtistViewSet(viewsets.ModelViewSet):
    model = Artist
    serializer_class = ArtistSerializer

from django.contrib.auth.models import User, Group
