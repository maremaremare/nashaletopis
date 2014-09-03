# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Mainpage.is_map_shown'
        db.add_column(u'main_mainpage', 'is_map_shown',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Mainpage.is_map_shown'
        db.delete_column(u'main_mainpage', 'is_map_shown')


    models = {
        u'main.mainpage': {
            'Meta': {'object_name': 'Mainpage'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'are_latest_stories_shown': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'hotline': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_hotline_shown': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_map_shown': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_photoalbum_shown': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'our_mission': ('django.db.models.fields.TextField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['main']