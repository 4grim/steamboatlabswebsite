# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TeamMember'
        db.create_table(u'about_teammember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'about', ['TeamMember'])

        # Adding model 'Link'
        db.create_table(u'about_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(default='True', max_length=100)),
            ('teammember', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['about.TeamMember'])),
        ))
        db.send_create_signal(u'about', ['Link'])

        # Adding model 'Media'
        db.create_table(u'about_media', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('publication', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('quote', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'about', ['Media'])


    def backwards(self, orm):
        # Deleting model 'TeamMember'
        db.delete_table(u'about_teammember')

        # Deleting model 'Link'
        db.delete_table(u'about_link')

        # Deleting model 'Media'
        db.delete_table(u'about_media')


    models = {
        u'about.link': {
            'Meta': {'object_name': 'Link'},
            'icon': ('django.db.models.fields.files.ImageField', [], {'default': "'True'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'teammember': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['about.TeamMember']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'about.media': {
            'Meta': {'object_name': 'Media'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'quote': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'about.teammember': {
            'Meta': {'object_name': 'TeamMember'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['about']