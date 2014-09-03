# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Location.region_root'
        db.delete_column(u'locations_location', 'region_root')

        # Deleting field 'Location.region'
        db.delete_column(u'locations_location', 'region')

        # Deleting field 'Location.show_in_sidebar'
        db.delete_column(u'locations_location', 'show_in_sidebar')


    def backwards(self, orm):
        # Adding field 'Location.region_root'
        db.add_column(u'locations_location', 'region_root',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Location.region'
        db.add_column(u'locations_location', 'region',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Location.show_in_sidebar'
        db.add_column(u'locations_location', 'show_in_sidebar',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    models = {
        u'locations.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django_ymap.fields.YmapCoord', [], {'max_length': '200', 'null': 'True', 'start_query': "u'\\u0420\\u043e\\u0441\\u0441\\u0438\\u044f'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['locations.Location']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['locations']