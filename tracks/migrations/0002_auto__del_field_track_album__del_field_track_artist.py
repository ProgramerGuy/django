# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Track.album'
        db.delete_column(u'tracks_track', 'album_id')

        # Deleting field 'Track.artist'
        db.delete_column(u'tracks_track', 'artist_id')


    def backwards(self, orm):
        # Adding field 'Track.album'
        db.add_column(u'tracks_track', 'album',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['albums.Album']),
                      keep_default=False)

        # Adding field 'Track.artist'
        db.add_column(u'tracks_track', 'artist',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['artists.Artist']),
                      keep_default=False)


    models = {
        u'tracks.track': {
            'Meta': {'object_name': 'Track'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'track_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['tracks']