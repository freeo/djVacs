# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Experiment'
        db.create_table('eyevacs_experiment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('eyevacs', ['Experiment'])

        # Adding model 'Participant'
        db.create_table('eyevacs_participant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('genuine', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('group', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('begin_radio_recent', self.gf('django.db.models.fields.IntegerField')()),
            ('begin_radio_bool', self.gf('django.db.models.fields.IntegerField')()),
            ('begin_radio_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('begin_radio_searchdepth', self.gf('django.db.models.fields.IntegerField')()),
            ('begin_likert_services', self.gf('django.db.models.fields.IntegerField')()),
            ('begin_likert_alikeness', self.gf('django.db.models.fields.IntegerField')()),
            ('begin_likert_importance', self.gf('django.db.models.fields.IntegerField')()),
            ('begin_likert_regret', self.gf('django.db.models.fields.IntegerField')()),
            ('ct_id', self.gf('django.db.models.fields.CharField')(max_length=81)),
            ('ct_choice', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('hc_id', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('hc_choice', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('ts_list', self.gf('django.db.models.fields.CharField')(max_length=111)),
            ('ts_choice', self.gf('django.db.models.fields.IntegerField')()),
            ('ts_order', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('scale_rnd_id', self.gf('django.db.models.fields.IntegerField')()),
            ('scale_rnd_order', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('scale_max_regret', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('heur_choice', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('demo_gender', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('demo_student_bool', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('demo_semester', self.gf('django.db.models.fields.IntegerField')()),
            ('demo_age', self.gf('django.db.models.fields.IntegerField')()),
            ('pg_time', self.gf('django.db.models.fields.CharField')(max_length=323)),
            ('pg_order', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('experiment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eyevacs.Experiment'])),
        ))
        db.send_create_signal('eyevacs', ['Participant'])

        # Adding model 'Attribute'
        db.create_table('eyevacs_attribute', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('exp_setup', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eyevacs.Experiment'])),
            ('position', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal('eyevacs', ['Attribute'])

        # Adding model 'Level'
        db.create_table('eyevacs_level', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link_attribute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eyevacs.Attribute'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('eyevacs', ['Level'])

        # Adding model 'External_Source_Data'
        db.create_table('eyevacs_external_source_data', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filetype', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('header', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('exp_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('experiment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eyevacs.Experiment'])),
        ))
        db.send_create_signal('eyevacs', ['External_Source_Data'])

        # Adding model 'External_Choice_Task'
        db.create_table('eyevacs_external_choice_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_hard', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ext_src_data', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eyevacs.External_Source_Data'])),
            ('ext_src_data_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('a1', self.gf('django.db.models.fields.CharField')(default='empty', max_length=15)),
            ('a2', self.gf('django.db.models.fields.CharField')(default='empty', max_length=15)),
            ('a3', self.gf('django.db.models.fields.CharField')(default='empty', max_length=15)),
            ('a4', self.gf('django.db.models.fields.CharField')(default='empty', max_length=15)),
            ('a5', self.gf('django.db.models.fields.CharField')(default='empty', max_length=15)),
            ('a6', self.gf('django.db.models.fields.CharField')(default='empty', max_length=15)),
            ('a7', self.gf('django.db.models.fields.CharField')(default='empty', max_length=15)),
            ('a8', self.gf('django.db.models.fields.CharField')(default='empty', max_length=15)),
            ('used', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('linked_pcpt', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eyevacs.Participant'], null=True, blank=True)),
            ('raw_src_line', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('eyevacs', ['External_Choice_Task'])

        # Adding model 'External_Order_Scale'
        db.create_table('eyevacs_external_order_scale', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_hard', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('scale_rnd_order_ext', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('linked_pcpt', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eyevacs.Participant'])),
        ))
        db.send_create_signal('eyevacs', ['External_Order_Scale'])


    def backwards(self, orm):
        # Deleting model 'Experiment'
        db.delete_table('eyevacs_experiment')

        # Deleting model 'Participant'
        db.delete_table('eyevacs_participant')

        # Deleting model 'Attribute'
        db.delete_table('eyevacs_attribute')

        # Deleting model 'Level'
        db.delete_table('eyevacs_level')

        # Deleting model 'External_Source_Data'
        db.delete_table('eyevacs_external_source_data')

        # Deleting model 'External_Choice_Task'
        db.delete_table('eyevacs_external_choice_task')

        # Deleting model 'External_Order_Scale'
        db.delete_table('eyevacs_external_order_scale')


    models = {
        'eyevacs.attribute': {
            'Meta': {'object_name': 'Attribute'},
            'exp_setup': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eyevacs.Experiment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        'eyevacs.experiment': {
            'Meta': {'object_name': 'Experiment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'eyevacs.external_choice_task': {
            'Meta': {'object_name': 'External_Choice_Task'},
            'a1': ('django.db.models.fields.CharField', [], {'default': "'empty'", 'max_length': '15'}),
            'a2': ('django.db.models.fields.CharField', [], {'default': "'empty'", 'max_length': '15'}),
            'a3': ('django.db.models.fields.CharField', [], {'default': "'empty'", 'max_length': '15'}),
            'a4': ('django.db.models.fields.CharField', [], {'default': "'empty'", 'max_length': '15'}),
            'a5': ('django.db.models.fields.CharField', [], {'default': "'empty'", 'max_length': '15'}),
            'a6': ('django.db.models.fields.CharField', [], {'default': "'empty'", 'max_length': '15'}),
            'a7': ('django.db.models.fields.CharField', [], {'default': "'empty'", 'max_length': '15'}),
            'a8': ('django.db.models.fields.CharField', [], {'default': "'empty'", 'max_length': '15'}),
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'ext_src_data': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eyevacs.External_Source_Data']"}),
            'ext_src_data_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_hard': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'linked_pcpt': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eyevacs.Participant']", 'null': 'True', 'blank': 'True'}),
            'raw_src_line': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'eyevacs.external_order_scale': {
            'Meta': {'object_name': 'External_Order_Scale'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_hard': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'linked_pcpt': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eyevacs.Participant']"}),
            'scale_rnd_order_ext': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'eyevacs.external_source_data': {
            'Meta': {'object_name': 'External_Source_Data'},
            'exp_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'experiment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eyevacs.Experiment']"}),
            'filetype': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'eyevacs.level': {
            'Meta': {'object_name': 'Level'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eyevacs.Attribute']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'eyevacs.participant': {
            'Meta': {'object_name': 'Participant'},
            'begin_likert_alikeness': ('django.db.models.fields.IntegerField', [], {}),
            'begin_likert_importance': ('django.db.models.fields.IntegerField', [], {}),
            'begin_likert_regret': ('django.db.models.fields.IntegerField', [], {}),
            'begin_likert_services': ('django.db.models.fields.IntegerField', [], {}),
            'begin_radio_bool': ('django.db.models.fields.IntegerField', [], {}),
            'begin_radio_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'begin_radio_recent': ('django.db.models.fields.IntegerField', [], {}),
            'begin_radio_searchdepth': ('django.db.models.fields.IntegerField', [], {}),
            'ct_choice': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'ct_id': ('django.db.models.fields.CharField', [], {'max_length': '81'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'demo_age': ('django.db.models.fields.IntegerField', [], {}),
            'demo_gender': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'demo_semester': ('django.db.models.fields.IntegerField', [], {}),
            'demo_student_bool': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'experiment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eyevacs.Experiment']"}),
            'genuine': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hc_choice': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'hc_id': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'heur_choice': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pg_order': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pg_time': ('django.db.models.fields.CharField', [], {'max_length': '323'}),
            'scale_max_regret': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'scale_rnd_id': ('django.db.models.fields.IntegerField', [], {}),
            'scale_rnd_order': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ts_choice': ('django.db.models.fields.IntegerField', [], {}),
            'ts_list': ('django.db.models.fields.CharField', [], {'max_length': '111'}),
            'ts_order': ('django.db.models.fields.CharField', [], {'max_length': '13'})
        }
    }

    complete_apps = ['eyevacs']