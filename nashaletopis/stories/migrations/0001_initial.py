# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'History_period'
        db.create_table(u'stories_history_period', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['stories.History_period'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'stories', ['History_period'])

        # Adding model 'Story'
        db.create_table(u'stories_story', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('birthyear', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('period', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='stories', null=True, to=orm['stories.History_period'])),
            ('radioprogram', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['radio.Radio'], null=True, blank=True)),
            ('audio', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('is_letter', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'stories', ['Story'])

        # Adding M2M table for field location on 'Story'
        m2m_table_name = db.shorten_name(u'stories_story_location')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('story', models.ForeignKey(orm[u'stories.story'], null=False)),
            ('location', models.ForeignKey(orm[u'locations.location'], null=False))
        ))
        db.create_unique(m2m_table_name, ['story_id', 'location_id'])

        # Adding model 'StoryActive'
        db.create_table(u'stories_storyactive', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('birthyear', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='stories_active', null=True, to=orm['locations.Location'])),
            ('radioprogram', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='stories', null=True, to=orm['radio.Radio'])),
            ('audio', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('is_letter', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'stories', ['StoryActive'])

        # Adding model 'Photo'
        db.create_table(u'stories_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('story', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='photos', null=True, to=orm['stories.Story'])),
            ('activestory', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='photos', null=True, to=orm['stories.StoryActive'])),
        ))
        db.send_create_signal(u'stories', ['Photo'])

        # Adding model 'Video'
        db.create_table(u'stories_video', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('video', self.gf('embed_video.fields.EmbedVideoField')(max_length=200)),
            ('story', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stories.Story'], null=True, blank=True)),
            ('activestory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stories.StoryActive'], null=True, blank=True)),
        ))
        db.send_create_signal(u'stories', ['Video'])


    def backwards(self, orm):
        # Deleting model 'History_period'
        db.delete_table(u'stories_history_period')

        # Deleting model 'Story'
        db.delete_table(u'stories_story')

        # Removing M2M table for field location on 'Story'
        db.delete_table(db.shorten_name(u'stories_story_location'))

        # Deleting model 'StoryActive'
        db.delete_table(u'stories_storyactive')

        # Deleting model 'Photo'
        db.delete_table(u'stories_photo')

        # Deleting model 'Video'
        db.delete_table(u'stories_video')


    models = {
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
        },
        u'stories.history_period': {
            'Meta': {'object_name': 'History_period'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['stories.History_period']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'stories.photo': {
            'Meta': {'object_name': 'Photo'},
            'activestory': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photos'", 'null': 'True', 'to': u"orm['stories.StoryActive']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photos'", 'null': 'True', 'to': u"orm['stories.Story']"})
        },
        u'stories.story': {
            'Meta': {'object_name': 'Story'},
            'audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'birthyear': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_letter': ('django.db.models.fields.BooleanField', [], {}),
            'location': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'stories'", 'symmetrical': 'False', 'to': u"orm['locations.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'stories'", 'null': 'True', 'to': u"orm['stories.History_period']"}),
            'radioprogram': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['radio.Radio']", 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'stories.storyactive': {
            'Meta': {'object_name': 'StoryActive'},
            'audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'birthyear': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_letter': ('django.db.models.fields.BooleanField', [], {}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stories_active'", 'null': 'True', 'to': u"orm['locations.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'radioprogram': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'stories'", 'null': 'True', 'to': u"orm['radio.Radio']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'stories.video': {
            'Meta': {'object_name': 'Video'},
            'activestory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stories.StoryActive']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stories.Story']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'video': ('embed_video.fields.EmbedVideoField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['stories']