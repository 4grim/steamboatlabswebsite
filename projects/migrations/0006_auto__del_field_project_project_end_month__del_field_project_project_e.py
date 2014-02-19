# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Project.project_end_month'
        db.delete_column(u'projects_project', 'project_end_month')

        # Deleting field 'Project.project_end_year'
        db.delete_column(u'projects_project', 'project_end_year')

        # Deleting field 'Project.project_start_month'
        db.delete_column(u'projects_project', 'project_start_month')

        # Deleting field 'Project.project_start_year'
        db.delete_column(u'projects_project', 'project_start_year')

        # Adding field 'Project.project_start'
        db.add_column(u'projects_project', 'project_start',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 18, 0, 0)),
                      keep_default=False)

        # Adding field 'Project.project_end'
        db.add_column(u'projects_project', 'project_end',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 18, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Project.project_end_month'
        db.add_column(u'projects_project', 'project_end_month',
                      self.gf('django.db.models.fields.CharField')(default='January', max_length=9),
                      keep_default=False)

        # Adding field 'Project.project_end_year'
        db.add_column(u'projects_project', 'project_end_year',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=2014, max_length=4),
                      keep_default=False)

        # Adding field 'Project.project_start_month'
        db.add_column(u'projects_project', 'project_start_month',
                      self.gf('django.db.models.fields.CharField')(default='January', max_length=9),
                      keep_default=False)

        # Adding field 'Project.project_start_year'
        db.add_column(u'projects_project', 'project_start_year',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=2013, max_length=4),
                      keep_default=False)

        # Deleting field 'Project.project_start'
        db.delete_column(u'projects_project', 'project_start')

        # Deleting field 'Project.project_end'
        db.delete_column(u'projects_project', 'project_end')


    models = {
        u'projects.client': {
            'Meta': {'object_name': 'Client'},
            'company_logo': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'company_website': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'testimonial': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'projects.medialink': {
            'Meta': {'object_name': 'MediaLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Project']", 'null': 'True'}),
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