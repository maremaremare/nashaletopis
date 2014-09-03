# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Mainpage.is_social_shown'
        db.add_column(u'main_mainpage', 'is_social_shown',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Mainpage.facebook'
        db.add_column(u'main_mainpage', 'facebook',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Mainpage.vkontakte'
        db.add_column(u'main_mainpage', 'vkontakte',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Mainpage.twitter'
        db.add_column(u'main_mainpage', 'twitter',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Mainpage.instagram'
        db.add_column(u'main_mainpage', 'instagram',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Mainpage.livejournal'
        db.add_column(u'main_mainpage', 'livejournal',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Mainpage.is_social_shown'
        db.delete_column(u'main_mainpage', 'is_social_shown')

        # Deleting field 'Mainpage.facebook'
        db.delete_column(u'main_mainpage', 'facebook')

        # Deleting field 'Mainpage.vkontakte'
        db.delete_column(u'main_mainpage', 'vkontakte')

        # Deleting field 'Mainpage.twitter'
        db.delete_column(u'main_mainpage', 'twitter')

        # Deleting field 'Mainpage.instagram'
        db.delete_column(u'main_mainpage', 'instagram')

        # Deleting field 'Mainpage.livejournal'
        db.delete_column(u'main_mainpage', 'livejournal')


    models = {
        u'main.mainpage': {
            'Meta': {'object_name': 'Mainpage'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'are_latest_stories_shown': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'hotline': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instagram': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'is_hotline_shown': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_map_shown': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_photoalbum_shown': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_social_shown': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'livejournal': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'our_mission': ('django.db.models.fields.TextField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'vkontakte': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']