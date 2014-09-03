# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'HelpingOrganisation.text'
        db.alter_column(u'helpmap_helpingorganisation', 'text', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'HelpingOrganisation.location'
        db.alter_column(u'helpmap_helpingorganisation', 'location_id', self.gf('mptt.fields.TreeForeignKey')(default=1, to=orm['locations.Location']))
        # Adding field 'HelpNeeded.opened'
        db.add_column(u'helpmap_helpneeded', 'opened',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


        # Changing field 'HelpNeeded.location'
        db.alter_column(u'helpmap_helpneeded', 'location_id', self.gf('mptt.fields.TreeForeignKey')(default=1, to=orm['locations.Location']))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'HelpingOrganisation.text'
        raise RuntimeError("Cannot reverse this migration. 'HelpingOrganisation.text' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'HelpingOrganisation.text'
        db.alter_column(u'helpmap_helpingorganisation', 'text', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HelpingOrganisation.location'
        db.alter_column(u'helpmap_helpingorganisation', 'location_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['locations.Location']))
        # Deleting field 'HelpNeeded.opened'
        db.delete_column(u'helpmap_helpneeded', 'opened')


        # Changing field 'HelpNeeded.location'
        db.alter_column(u'helpmap_helpneeded', 'location_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['locations.Location']))

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
            'location': ('mptt.fields.TreeForeignKey', [], {'related_name': "'helpgiven'", 'to': u"orm['locations.Location']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'helpmap.helpneeded': {
            'Meta': {'object_name': 'HelpNeeded'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'location': ('mptt.fields.TreeForeignKey', [], {'related_name': "'helpneeded'", 'to': u"orm['locations.Location']"}),
            'opened': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
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
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['helpmap']