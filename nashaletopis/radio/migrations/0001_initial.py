# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Radio_category'
        db.create_table(u'radio_radio_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'radio', ['Radio_category'])

        # Adding model 'Radio'
        db.create_table(u'radio_radio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('participants', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('audio', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['radio.Radio_category'])),
        ))
        db.send_create_signal(u'radio', ['Radio'])

        # Adding model 'Announcement_radio'
        db.create_table(u'radio_announcement_radio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'radio', ['Announcement_radio'])


    def backwards(self, orm):
        # Deleting model 'Radio_category'
        db.delete_table(u'radio_radio_category')

        # Deleting model 'Radio'
        db.delete_table(u'radio_radio')

        # Deleting model 'Announcement_radio'
        db.delete_table(u'radio_announcement_radio')


    models = {
        u'radio.announcement_radio': {
            'Meta': {'object_name': 'Announcement_radio'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'radio.radio': {
            'Meta': {'object_name': 'Radio'},
            'audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['radio.Radio_category']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participants': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'radio.radio_category': {
            'Meta': {'object_name': 'Radio_category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['radio']