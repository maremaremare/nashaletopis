# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Story.period'
        db.delete_column(u'stories_story', 'period_id')

        # Adding M2M table for field period on 'Story'
        m2m_table_name = db.shorten_name(u'stories_story_period')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('story', models.ForeignKey(orm[u'stories.story'], null=False)),
            ('history_period', models.ForeignKey(orm[u'stories.history_period'], null=False))
        ))
        db.create_unique(m2m_table_name, ['story_id', 'history_period_id'])


    def backwards(self, orm):
        # Adding field 'Story.period'
        db.add_column(u'stories_story', 'period',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='stories', null=True, to=orm['stories.History_period'], blank=True),
                      keep_default=False)

        # Removing M2M table for field period on 'Story'
        db.delete_table(db.shorten_name(u'stories_story_period'))


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
        },
        u'radio.radio': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Radio'},
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
            'Meta': {'ordering': "['photo']", 'object_name': 'Photo'},
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
            'location': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'stories'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['locations.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'period': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'stories'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['stories.History_period']"}),
            'radioprogram': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['radio.Radio']", 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'stories.storyactive': {
            'Meta': {'object_name': 'StoryActive'},
            'audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'birthyear': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_letter': ('django.db.models.fields.BooleanField', [], {}),
            'location': ('mptt.fields.TreeForeignKey', [], {'related_name': "'stories_active'", 'null': 'True', 'to': u"orm['locations.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'radioprogram': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'stories'", 'null': 'True', 'to': u"orm['radio.Radio']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'stories.video': {
            'Meta': {'object_name': 'Video'},
            'activestory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stories.StoryActive']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'videos'", 'null': 'True', 'to': u"orm['stories.Story']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'video': ('embed_video.fields.EmbedVideoField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['stories']