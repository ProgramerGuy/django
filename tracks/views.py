from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
import json
#import ipdb; ipdb.set_trace()

from .models import Track
from rest_framework import viewsets

class TrackViewSet(viewsets.ModelViewSet):
    model = Track


def track_view(request, title):
    track = get_object_or_404(Track,title = title)
    data = {
        'title': track.title,
        'order': track.order,
        'album': track.album.title,
        'artist': {
            'name': track.artist.first_name,
            'bio': track.artist.biography,
        }
    }

    return render(request, 'track.html', {'track': track})

    #json.loads(string_json) esto convierte de json a diccionario de python'''
    #Conversion de diccionario de python a json'''
    #json_data = json.dumps(data)

    #return HttpResponse(json_data, content_type='aplication/json')
