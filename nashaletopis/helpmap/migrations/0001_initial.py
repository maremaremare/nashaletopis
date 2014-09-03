# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HelpingCategory'
        db.create_table(u'helpmap_helpingcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'helpmap', ['HelpingCategory'])

        # Adding model 'HelpingOrganisation'
        db.create_table(u'helpmap_helpingorganisation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['helpmap.HelpingCategory'])),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='helpgiven', null=True, to=orm['locations.Location'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'helpmap', ['HelpingOrganisation'])

        # Adding model 'HelpNeeded'
        db.create_table(u'helpmap_helpneeded', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='helpneeded', null=True, to=orm['locations.Location'])),
        ))
        db.send_create_signal(u'helpmap', ['HelpNeeded'])


    def backwards(self, orm):
        # Deleting model 'HelpingCategory'
        db.delete_table(u'helpmap_helpingcategory')

        # Deleting model 'HelpingOrganisation'
        db.delete_table(u'helpmap_helpingorganisation')

        # Deleting model 'HelpNeeded'
        db.delete_table(u'helpmap_helpneeded')


    models = {
        u'helpmap.helpingcategory': {
            'Meta': {'object_name': 'HelpingCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'helpmap.helpingorganisation': {
            'Meta': {'object_name': 'HelpingOrganisation'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['helpmap.HelpingCategory']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'helpgiven'", 'null': 'True', 'to': u"orm['locations.Location']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'helpmap.helpneeded': {
            'Meta': {'object_name': 'HelpNeeded'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'helpneeded'", 'null': 'True', 'to': u"orm['locations.Location']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'locations.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django_ymap.fields.YmapCoord', [], {'max_length': '200', 'null': 'True', 'start_query': "u'\\u0420\\u043e\\u0441\\u0441\\u0438\\u044f'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['locations.Location']"}),
            'region': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'region_root': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'show_in_sidebar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['helpmap']