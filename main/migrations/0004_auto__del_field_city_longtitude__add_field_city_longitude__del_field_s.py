# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'City.longtitude'
        db.delete_column(u'main_city', 'longtitude')

        # Adding field 'City.longitude'
        db.add_column(u'main_city', 'longitude',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Deleting field 'StateCapital.longtitude'
        db.delete_column(u'main_statecapital', 'longtitude')

        # Adding field 'StateCapital.longitude'
        db.add_column(u'main_statecapital', 'longitude',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'City.longtitude'
        db.add_column(u'main_city', 'longtitude',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Deleting field 'City.longitude'
        db.delete_column(u'main_city', 'longitude')

        # Adding field 'StateCapital.longtitude'
        db.add_column(u'main_statecapital', 'longtitude',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Deleting field 'StateCapital.longitude'
        db.delete_column(u'main_statecapital', 'longitude')


    models = {
        u'main.city': {
            'Meta': {'object_name': 'City'},
            'county': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.State']", 'null': 'True'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'main.state': {
            'Meta': {'object_name': 'State'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'main.statecapital': {
            'Meta': {'object_name': 'StateCapital'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.State']", 'unique': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['main']