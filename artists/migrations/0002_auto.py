# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field favorite_songs on 'Artist'
        db.delete_table(db.shorten_name(u'artists_artist_favorite_songs'))


    def backwards(self, orm):
        # Adding M2M table for field favorite_songs on 'Artist'
        m2m_table_name = db.shorten_name(u'artists_artist_favorite_songs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('artist', models.ForeignKey(orm[u'artists.artist'], null=False)),
            ('track', models.ForeignKey(orm[u'tracks.track'], null=False))
        ))
        db.create_unique(m2m_table_name, ['artist_id', 'track_id'])


    models = {
        u'artists.artist': {
            'Meta': {'object_name': 'Artist'},
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['artists']