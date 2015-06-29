from django.contrib import admin
from tracks.models import Track
from albums.models import Album
from .models import Artist

class TrackInLine(admin.StackedInline):
    model = Track
    extra = 1

class AlbumInLine(admin.StackedInline):
    model = Album
    extra = 1

class ArtistAdmin(admin.ModelAdmin):
    search_fields = ('first_name','last_name')
    filter_vertical = ('favorite_songs', )
    inlines = [TrackInLine, AlbumInLine]


admin.site.register(Artist,ArtistAdmin)
