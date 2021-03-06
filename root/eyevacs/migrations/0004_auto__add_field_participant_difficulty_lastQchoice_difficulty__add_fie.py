# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Participant.difficulty_lastQchoice_difficulty'
        db.add_column('eyevacs_participant', 'difficulty_lastQchoice_difficulty',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.difficulty_lastQfrustration'
        db.add_column('eyevacs_participant', 'difficulty_lastQfrustration',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.difficulty_lastQhesitation'
        db.add_column('eyevacs_participant', 'difficulty_lastQhesitation',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.difficulty_lastQsimilarity'
        db.add_column('eyevacs_participant', 'difficulty_lastQsimilarity',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.t_pl_difficulty_last'
        db.add_column('eyevacs_participant', 't_pl_difficulty_last',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.holdout1'
        db.add_column('eyevacs_participant', 'holdout1',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.t_holdout1'
        db.add_column('eyevacs_participant', 't_holdout1',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.t_loadingholdout'
        db.add_column('eyevacs_participant', 't_loadingholdout',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.holdout2'
        db.add_column('eyevacs_participant', 'holdout2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.t_holdout2'
        db.add_column('eyevacs_participant', 't_holdout2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.favpackage_food'
        db.add_column('eyevacs_participant', 'favpackage_food',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.favpackage_recommending'
        db.add_column('eyevacs_participant', 'favpackage_recommending',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.favpackage_distance'
        db.add_column('eyevacs_participant', 'favpackage_distance',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.favpackage_seaview'
        db.add_column('eyevacs_participant', 'favpackage_seaview',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.favpackage_price'
        db.add_column('eyevacs_participant', 'favpackage_price',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.favpackage_room'
        db.add_column('eyevacs_participant', 'favpackage_room',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.t_favpackage'
        db.add_column('eyevacs_participant', 't_favpackage',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.hlout1pk'
        db.add_column('eyevacs_participant', 'hlout1pk',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.hlout1a1'
        db.add_column('eyevacs_participant', 'hlout1a1',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.hlout1a2'
        db.add_column('eyevacs_participant', 'hlout1a2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.hlout1a3'
        db.add_column('eyevacs_participant', 'hlout1a3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.hlout2pk'
        db.add_column('eyevacs_participant', 'hlout2pk',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.hlout2a1'
        db.add_column('eyevacs_participant', 'hlout2a1',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.hlout2a2'
        db.add_column('eyevacs_participant', 'hlout2a2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Participant.hlout2a3'
        db.add_column('eyevacs_participant', 'hlout2a3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Participant.difficulty_lastQchoice_difficulty'
        db.delete_column('eyevacs_participant', 'difficulty_lastQchoice_difficulty')

        # Deleting field 'Participant.difficulty_lastQfrustration'
        db.delete_column('eyevacs_participant', 'difficulty_lastQfrustration')

        # Deleting field 'Participant.difficulty_lastQhesitation'
        db.delete_column('eyevacs_participant', 'difficulty_lastQhesitation')

        # Deleting field 'Participant.difficulty_lastQsimilarity'
        db.delete_column('eyevacs_participant', 'difficulty_lastQsimilarity')

        # Deleting field 'Participant.t_pl_difficulty_last'
        db.delete_column('eyevacs_participant', 't_pl_difficulty_last')

        # Deleting field 'Participant.holdout1'
        db.delete_column('eyevacs_participant', 'holdout1')

        # Deleting field 'Participant.t_holdout1'
        db.delete_column('eyevacs_participant', 't_holdout1')

        # Deleting field 'Participant.t_loadingholdout'
        db.delete_column('eyevacs_participant', 't_loadingholdout')

        # Deleting field 'Participant.holdout2'
        db.delete_column('eyevacs_participant', 'holdout2')

        # Deleting field 'Participant.t_holdout2'
        db.delete_column('eyevacs_participant', 't_holdout2')

        # Deleting field 'Participant.favpackage_food'
        db.delete_column('eyevacs_participant', 'favpackage_food')

        # Deleting field 'Participant.favpackage_recommending'
        db.delete_column('eyevacs_participant', 'favpackage_recommending')

        # Deleting field 'Participant.favpackage_distance'
        db.delete_column('eyevacs_participant', 'favpackage_distance')

        # Deleting field 'Participant.favpackage_seaview'
        db.delete_column('eyevacs_participant', 'favpackage_seaview')

        # Deleting field 'Participant.favpackage_price'
        db.delete_column('eyevacs_participant', 'favpackage_price')

        # Deleting field 'Participant.favpackage_room'
        db.delete_column('eyevacs_participant', 'favpackage_room')

        # Deleting field 'Participant.t_favpackage'
        db.delete_column('eyevacs_participant', 't_favpackage')

        # Deleting field 'Participant.hlout1pk'
        db.delete_column('eyevacs_participant', 'hlout1pk')

        # Deleting field 'Participant.hlout1a1'
        db.delete_column('eyevacs_participant', 'hlout1a1')

        # Deleting field 'Participant.hlout1a2'
        db.delete_column('eyevacs_participant', 'hlout1a2')

        # Deleting field 'Participant.hlout1a3'
        db.delete_column('eyevacs_participant', 'hlout1a3')

        # Deleting field 'Participant.hlout2pk'
        db.delete_column('eyevacs_participant', 'hlout2pk')

        # Deleting field 'Participant.hlout2a1'
        db.delete_column('eyevacs_participant', 'hlout2a1')

        # Deleting field 'Participant.hlout2a2'
        db.delete_column('eyevacs_participant', 'hlout2a2')

        # Deleting field 'Participant.hlout2a3'
        db.delete_column('eyevacs_participant', 'hlout2a3')


    models = {
        'eyevacs.attribute': {
            'Meta': {'object_name': 'Attribute'},
            'exp_setup': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eyevacs.Experiment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        'eyevacs.experiment': {
            'Meta': {'object_name': 'Experiment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'eyevacs.external_baseline_choice_task': {
            'Meta': {'object_name': 'External_Baseline_Choice_Task'},
            'a1': ('django.db.models.fields.CharField', [], {'default': "'empty'", 'max_length': '15'}),
            'a2': ('django.db.models.fields.CharField', [], {'default': "'empty'", 'max_length': '15'}),
            'a3': ('django.db.models.fields.CharField', [], {'default': "'empty'", 'max_length': '15'}),
            'a4': ('django.db.models.fields.CharField', [], {'default': "'empty'", 'max_length': '15'}),
            'a5': ('django.db.models.fields.CharField', [], {'default': "'empty'", 'max_length': '15'}),
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'ext_src_data': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eyevacs.External_Source_Data']"}),
            'ext_src_data_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_hard': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'linked_pcpt': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Baseline_Choice_TasksAsParticipant'", 'null': 'True', 'to': "orm['eyevacs.Participant']"}),
            'linked_pub': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Baseline_Choice_TasksAsPub'", 'null': 'True', 'to': "orm['eyevacs.Pub']"}),
            'raw_src_line': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'task': ('django.db.models.fields.IntegerField', [], {}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
            'linked_pcpt': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Choice_TasksAsParticipant'", 'null': 'True', 'to': "orm['eyevacs.Participant']"}),
            'linked_pub': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Choice_TasksAsPub'", 'null': 'True', 'to': "orm['eyevacs.Pub']"}),
            'raw_src_line': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'eyevacs.external_order_scale': {
            'Meta': {'object_name': 'External_Order_Scale'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_hard': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'linked_pcpt': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eyevacs.Participant']", 'null': 'True', 'blank': 'True'}),
            'linked_pub': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eyevacs.Pub']", 'null': 'True', 'blank': 'True'}),
            'scale_rnd_order_ext': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'source_file': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eyevacs.External_Source_Data']", 'null': 'True', 'blank': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'eyevacs.external_source_data': {
            'Meta': {'object_name': 'External_Source_Data'},
            'exp_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'experiment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eyevacs.Experiment']"}),
            'filetype': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'range_end': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'range_start': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'eyevacs.grouping': {
            'Meta': {'object_name': 'Grouping'},
            'counter': ('django.db.models.fields.IntegerField', [], {}),
            'experiment': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['eyevacs.Experiment']", 'unique': 'True'}),
            'group_nr': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_hole_history': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id_holes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seed': ('django.db.models.fields.IntegerField', [], {})
        },
        'eyevacs.level': {
            'Meta': {'object_name': 'Level'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eyevacs.Attribute']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'eyevacs.participant': {
            'Meta': {'object_name': 'Participant'},
            'begin_time': ('django.db.models.fields.DateTimeField', [], {}),
            'ct1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct10': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct10a1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct10a2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct10a3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct10a4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct10a5': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct10amount': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct10pk': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct11': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct11a1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct11a2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct11a3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct11a4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct11a5': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct11amount': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct11pk': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct12': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct12a1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct12a2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct12a3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct12a4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct12a5': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct12amount': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct12pk': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct13': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct13a1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct13a2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct13a3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct13a4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct13a5': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct13amount': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct13pk': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct14': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct14a1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct14a2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct14a3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct14a4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct14a5': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct14amount': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct14pk': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct15': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct15a1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct15a2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct15a3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct15a4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct15a5': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct15amount': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct15pk': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct16': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct16a1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct16a2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct16a3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct16a4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct16a5': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct16amount': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct16pk': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct1a1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct1a2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct1a3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct1a4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct1a5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct1amount': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct1pk': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct2a1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct2a2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct2a3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct2a4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct2a5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct2amount': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct2pk': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct3a1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct3a2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct3a3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct3a4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct3a5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct3amount': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct3pk': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct4a1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct4a2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct4a3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct4a4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct4a5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct4amount': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct4pk': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct5a1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct5a2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct5a3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct5a4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct5a5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct5amount': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct5pk': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct6': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct6a1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct6a2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct6a3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct6a4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct6a5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct6amount': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct6pk': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct7': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct7a1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct7a2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct7a3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct7a4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct7a5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct7amount': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct7pk': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct8': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct8a1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct8a2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct8a3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct8a4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct8a5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct8amount': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct8pk': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ct9': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct9a1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct9a2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct9a3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct9a4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct9a5': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct9amount': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct9pk': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ct_size': ('django.db.models.fields.IntegerField', [], {}),
            'ctamount1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ctamount10': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ctamount11': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ctamount12': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ctamount13': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ctamount14': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ctamount15': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ctamount16': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'ctamount2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ctamount3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ctamount4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ctamount5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ctamount6': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ctamount7': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ctamount8': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ctamount9': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'cttime1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cttime10': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'cttime11': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'cttime12': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'cttime13': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'cttime14': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'cttime15': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'cttime16': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'cttime2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cttime3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cttime4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cttime5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cttime6': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cttime7': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cttime8': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cttime9': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'def_group': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'demo_age': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'demo_gender': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'difficulty_lastQchoice_difficulty': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'difficulty_lastQfrustration': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'difficulty_lastQhesitation': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'difficulty_lastQsimilarity': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'experience_lastvacation': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'experience_planningvacation': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'experience_searchduration': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'experiment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eyevacs.Experiment']"}),
            'explanation_distance': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'explanation_food': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'explanation_price': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'explanation_recommend': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'explanation_room': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'explanation_view': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fav_distance': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fav_food': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fav_price': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fav_recommending': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fav_room': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fav_seaview': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'favpackage_distance': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'favpackage_food': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'favpackage_price': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'favpackage_recommending': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'favpackage_room': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'favpackage_seaview': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'h1conjoint1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'h1conjoint2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'h1conjoint3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'h1conjoint4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'h1conjoint5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'h1conjoint6': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'h1conjoint7': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'h1conjoint8': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'h2durationpath': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'h2searchpath': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'h2totaltime': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'h2transitdecision': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'hard_id': ('django.db.models.fields.IntegerField', [], {}),
            'hlout1a1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'hlout1a2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'hlout1a3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'hlout1pk': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'hlout2a1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'hlout2a2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'hlout2a3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'hlout2pk': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'holdout1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'holdout2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'override_group': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'raw_timestamps': ('django.db.models.fields.TextField', [], {'default': "'not assigned'"}),
            'rnd_happinessQ1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'rnd_happinessQ2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'rnd_happinessQ3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'rnd_happinessQ4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'rnd_happiness_order': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'rnd_happiness_order_pk': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'rnd_involvementQ1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_involvementQ2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_involvementQ3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_involvementQ4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_involvement_order': ('django.db.models.fields.TextField', [], {}),
            'rnd_involvement_order_pk': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_maxQ1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_maxQ2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_maxQ3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_maxQ4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_maxQ5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_maxQ6': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_max_order': ('django.db.models.fields.TextField', [], {}),
            'rnd_max_order_pk': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_regretQ1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_regretQ2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_regretQ3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_regretQ4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_regretQ5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_regret_order': ('django.db.models.fields.TextField', [], {}),
            'rnd_regret_order_pk': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_searchgoalsQ1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_searchgoalsQ2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_searchgoalsQ3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_searchgoalsQ4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_searchgoals_order': ('django.db.models.fields.TextField', [], {}),
            'rnd_searchgoals_order_pk': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            't_demographics': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_experience': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_expl_0_overview': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_expl_1_food': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_expl_2_recommend': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_expl_3_distance': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_expl_4_view': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_expl_5_price': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_expl_6_room': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_expl_7_fav': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_expl_8_ctseqintro': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_favpackage': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            't_h1page1': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_h1page2': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_h2transitdecision': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50', 'blank': 'True'}),
            't_holdout1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            't_holdout2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            't_loadingconjoint': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_loadingholdout': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            't_pl_difficulty_last': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            't_rnd_happiness': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_rnd_involvement': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_rnd_max': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_rnd_regret': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_rnd_searchgoals': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_welcome': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            'testpcpt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'total_time': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '100'}),
            'valid_pcpt': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'eyevacs.pub': {
            'Meta': {'object_name': 'Pub'},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'csrftoken': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'ct_size': ('django.db.models.fields.IntegerField', [], {}),
            'def_group': ('django.db.models.fields.IntegerField', [], {}),
            'experiment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eyevacs.Experiment']"}),
            'hard_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'override_group': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sessionid': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'eyevacs.scale': {
            'Meta': {'object_name': 'Scale'},
            'experiment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eyevacs.Experiment']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rnd_file': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['eyevacs.External_Source_Data']", 'unique': 'True', 'primary_key': 'True'})
        },
        'eyevacs.scale_question': {
            'Meta': {'object_name': 'Scale_Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_order': ('django.db.models.fields.IntegerField', [], {}),
            'linked_scale': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eyevacs.Scale']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['eyevacs']