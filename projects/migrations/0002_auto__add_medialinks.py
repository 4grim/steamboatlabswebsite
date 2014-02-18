# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MediaLinks'
        db.create_table(u'projects_medialinks', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publication', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('quote', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'projects', ['MediaLinks'])

        # Adding M2M table for field media_links on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_media_links')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('medialinks', models.ForeignKey(orm[u'projects.medialinks'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'medialinks_id'])


    def backwards(self, orm):
        # Deleting model 'MediaLinks'
        db.delete_table(u'projects_medialinks')

        # Removing M2M table for field media_links on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_media_links'))


    models = {
        u'projects.client': {
            'Meta': {'object_name': 'Client'},
            'company_logo': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'company_website': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'testimonial': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'projects.medialinks': {
            'Meta': {'object_name': 'MediaLinks'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'publication': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'quote': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'accomplishments': ('django.db.models.fields.TextField', [], {}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Client']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'feature_project': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['projects.ProjectImage']", 'symmetrical': 'False', 'blank': 'True'}),
            'media_links': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['projects.MediaLinks']", 'symmetrical': 'False', 'blank': 'True'}),
            'project_end': ('django.db.models.fields.DateField', [], {}),
            'project_start': ('django.db.models.fields.DateField', [], {}),
            'technologies': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'projects.projectimage': {
            'Meta': {'object_name': 'ProjectImage'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['projects']