# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Link.icon'
        db.add_column(u'about_link', 'icon',
                      self.gf('django.db.models.fields.files.ImageField')(default='True', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Link.icon'
        db.delete_column(u'about_link', 'icon')


    models = {
        u'about.link': {
            'Meta': {'object_name': 'Link'},
            'icon': ('django.db.models.fields.files.ImageField', [], {'default': "'True'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'teammember': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['about.TeamMember']"}),
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