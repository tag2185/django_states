# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'City'
        db.create_table(u'main_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('zip_code', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('longtitude', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal(u'main', ['City'])

        # Adding model 'StateCapital'
        db.create_table(u'main_statecapital', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('longtitude', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('population', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('state', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.State'], unique=True, null=True)),
        ))
        db.send_create_signal(u'main', ['StateCapital'])

        # Adding model 'State'
        db.create_table(u'main_state', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=2, null=True)),
        ))
        db.send_create_signal(u'main', ['State'])


    def backwards(self, orm):
        # Deleting model 'City'
        db.delete_table(u'main_city')

        # Deleting model 'StateCapital'
        db.delete_table(u'main_statecapital')

        # Deleting model 'State'
        db.delete_table(u'main_state')


    models = {
        u'main.city': {
            'Meta': {'object_name': 'City'},
            'county': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'longtitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
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
            'longtitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.State']", 'unique': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['main']