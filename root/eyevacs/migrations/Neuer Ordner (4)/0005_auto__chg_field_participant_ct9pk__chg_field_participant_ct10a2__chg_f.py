# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Participant.ct9pk'
        db.alter_column('eyevacs_participant', 'ct9pk', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct10a2'
        db.alter_column('eyevacs_participant', 'ct10a2', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct10a1'
        db.alter_column('eyevacs_participant', 'ct10a1', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct10a5'
        db.alter_column('eyevacs_participant', 'ct10a5', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct10a4'
        db.alter_column('eyevacs_participant', 'ct10a4', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.cttime9'
        db.alter_column('eyevacs_participant', 'cttime9', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct9a4'
        db.alter_column('eyevacs_participant', 'ct9a4', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ctamount13'
        db.alter_column('eyevacs_participant', 'ctamount13', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ctamount12'
        db.alter_column('eyevacs_participant', 'ctamount12', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.cttime15'
        db.alter_column('eyevacs_participant', 'cttime15', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.cttime14'
        db.alter_column('eyevacs_participant', 'cttime14', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.cttime16'
        db.alter_column('eyevacs_participant', 'cttime16', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.cttime11'
        db.alter_column('eyevacs_participant', 'cttime11', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.cttime10'
        db.alter_column('eyevacs_participant', 'cttime10', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.cttime13'
        db.alter_column('eyevacs_participant', 'cttime13', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.cttime12'
        db.alter_column('eyevacs_participant', 'cttime12', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct10pk'
        db.alter_column('eyevacs_participant', 'ct10pk', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct14a3'
        db.alter_column('eyevacs_participant', 'ct14a3', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct13pk'
        db.alter_column('eyevacs_participant', 'ct13pk', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct10a3'
        db.alter_column('eyevacs_participant', 'ct10a3', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct13amount'
        db.alter_column('eyevacs_participant', 'ct13amount', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct14a5'
        db.alter_column('eyevacs_participant', 'ct14a5', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct15pk'
        db.alter_column('eyevacs_participant', 'ct15pk', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct11a5'
        db.alter_column('eyevacs_participant', 'ct11a5', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct11a2'
        db.alter_column('eyevacs_participant', 'ct11a2', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct11a3'
        db.alter_column('eyevacs_participant', 'ct11a3', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct11a1'
        db.alter_column('eyevacs_participant', 'ct11a1', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.demo_age'
        db.alter_column('eyevacs_participant', 'demo_age', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.override_group'
        db.alter_column('eyevacs_participant', 'override_group', self.gf('django.db.models.fields.CharField')(default='', max_length=3))

        # Changing field 'Participant.ct9'
        db.alter_column('eyevacs_participant', 'ct9', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct9a5'
        db.alter_column('eyevacs_participant', 'ct9a5', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct9a1'
        db.alter_column('eyevacs_participant', 'ct9a1', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct9a2'
        db.alter_column('eyevacs_participant', 'ct9a2', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct9a3'
        db.alter_column('eyevacs_participant', 'ct9a3', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct16a4'
        db.alter_column('eyevacs_participant', 'ct16a4', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct11amount'
        db.alter_column('eyevacs_participant', 'ct11amount', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct15a2'
        db.alter_column('eyevacs_participant', 'ct15a2', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct15a3'
        db.alter_column('eyevacs_participant', 'ct15a3', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct15a4'
        db.alter_column('eyevacs_participant', 'ct15a4', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.rnd_happinessQ4'
        db.alter_column('eyevacs_participant', 'rnd_happinessQ4', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.rnd_happinessQ2'
        db.alter_column('eyevacs_participant', 'rnd_happinessQ2', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.rnd_happinessQ3'
        db.alter_column('eyevacs_participant', 'rnd_happinessQ3', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.rnd_happinessQ1'
        db.alter_column('eyevacs_participant', 'rnd_happinessQ1', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ctamount9'
        db.alter_column('eyevacs_participant', 'ctamount9', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct16amount'
        db.alter_column('eyevacs_participant', 'ct16amount', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct12a5'
        db.alter_column('eyevacs_participant', 'ct12a5', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct12a4'
        db.alter_column('eyevacs_participant', 'ct12a4', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct12a1'
        db.alter_column('eyevacs_participant', 'ct12a1', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct12a3'
        db.alter_column('eyevacs_participant', 'ct12a3', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.rnd_happiness_order'
        db.alter_column('eyevacs_participant', 'rnd_happiness_order', self.gf('django.db.models.fields.TextField')(max_length=100))

        # Changing field 'Participant.ct10amount'
        db.alter_column('eyevacs_participant', 'ct10amount', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct14a2'
        db.alter_column('eyevacs_participant', 'ct14a2', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct14amount'
        db.alter_column('eyevacs_participant', 'ct14amount', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct16'
        db.alter_column('eyevacs_participant', 'ct16', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct14'
        db.alter_column('eyevacs_participant', 'ct14', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct12'
        db.alter_column('eyevacs_participant', 'ct12', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct13'
        db.alter_column('eyevacs_participant', 'ct13', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct10'
        db.alter_column('eyevacs_participant', 'ct10', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct11'
        db.alter_column('eyevacs_participant', 'ct11', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct12a2'
        db.alter_column('eyevacs_participant', 'ct12a2', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct16pk'
        db.alter_column('eyevacs_participant', 'ct16pk', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct16a2'
        db.alter_column('eyevacs_participant', 'ct16a2', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct16a5'
        db.alter_column('eyevacs_participant', 'ct16a5', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct16a1'
        db.alter_column('eyevacs_participant', 'ct16a1', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct15amount'
        db.alter_column('eyevacs_participant', 'ct15amount', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct12pk'
        db.alter_column('eyevacs_participant', 'ct12pk', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct15a1'
        db.alter_column('eyevacs_participant', 'ct15a1', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct14pk'
        db.alter_column('eyevacs_participant', 'ct14pk', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct13a1'
        db.alter_column('eyevacs_participant', 'ct13a1', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct13a2'
        db.alter_column('eyevacs_participant', 'ct13a2', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct15'
        db.alter_column('eyevacs_participant', 'ct15', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct13a4'
        db.alter_column('eyevacs_participant', 'ct13a4', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct13a5'
        db.alter_column('eyevacs_participant', 'ct13a5', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct14a4'
        db.alter_column('eyevacs_participant', 'ct14a4', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct15a5'
        db.alter_column('eyevacs_participant', 'ct15a5', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct11a4'
        db.alter_column('eyevacs_participant', 'ct11a4', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.rnd_happiness_order_pk'
        db.alter_column('eyevacs_participant', 'rnd_happiness_order_pk', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct11pk'
        db.alter_column('eyevacs_participant', 'ct11pk', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct9amount'
        db.alter_column('eyevacs_participant', 'ct9amount', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct13a3'
        db.alter_column('eyevacs_participant', 'ct13a3', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct16a3'
        db.alter_column('eyevacs_participant', 'ct16a3', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ctamount14'
        db.alter_column('eyevacs_participant', 'ctamount14', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ctamount15'
        db.alter_column('eyevacs_participant', 'ctamount15', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ctamount16'
        db.alter_column('eyevacs_participant', 'ctamount16', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ctamount11'
        db.alter_column('eyevacs_participant', 'ctamount11', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct12amount'
        db.alter_column('eyevacs_participant', 'ct12amount', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ctamount10'
        db.alter_column('eyevacs_participant', 'ctamount10', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Participant.ct14a1'
        db.alter_column('eyevacs_participant', 'ct14a1', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'Participant.ct9pk'
        db.alter_column('eyevacs_participant', 'ct9pk', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct10a2'
        db.alter_column('eyevacs_participant', 'ct10a2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct10a1'
        db.alter_column('eyevacs_participant', 'ct10a1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct10a5'
        db.alter_column('eyevacs_participant', 'ct10a5', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct10a4'
        db.alter_column('eyevacs_participant', 'ct10a4', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.cttime9'
        db.alter_column('eyevacs_participant', 'cttime9', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct9a4'
        db.alter_column('eyevacs_participant', 'ct9a4', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ctamount13'
        db.alter_column('eyevacs_participant', 'ctamount13', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ctamount12'
        db.alter_column('eyevacs_participant', 'ctamount12', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.cttime15'
        db.alter_column('eyevacs_participant', 'cttime15', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.cttime14'
        db.alter_column('eyevacs_participant', 'cttime14', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.cttime16'
        db.alter_column('eyevacs_participant', 'cttime16', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.cttime11'
        db.alter_column('eyevacs_participant', 'cttime11', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.cttime10'
        db.alter_column('eyevacs_participant', 'cttime10', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.cttime13'
        db.alter_column('eyevacs_participant', 'cttime13', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.cttime12'
        db.alter_column('eyevacs_participant', 'cttime12', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct10pk'
        db.alter_column('eyevacs_participant', 'ct10pk', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct14a3'
        db.alter_column('eyevacs_participant', 'ct14a3', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct13pk'
        db.alter_column('eyevacs_participant', 'ct13pk', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct10a3'
        db.alter_column('eyevacs_participant', 'ct10a3', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct13amount'
        db.alter_column('eyevacs_participant', 'ct13amount', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct14a5'
        db.alter_column('eyevacs_participant', 'ct14a5', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct15pk'
        db.alter_column('eyevacs_participant', 'ct15pk', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct11a5'
        db.alter_column('eyevacs_participant', 'ct11a5', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct11a2'
        db.alter_column('eyevacs_participant', 'ct11a2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct11a3'
        db.alter_column('eyevacs_participant', 'ct11a3', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct11a1'
        db.alter_column('eyevacs_participant', 'ct11a1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.demo_age'
        db.alter_column('eyevacs_participant', 'demo_age', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Participant.override_group'
        db.alter_column('eyevacs_participant', 'override_group', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))

        # Changing field 'Participant.ct9'
        db.alter_column('eyevacs_participant', 'ct9', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct9a5'
        db.alter_column('eyevacs_participant', 'ct9a5', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct9a1'
        db.alter_column('eyevacs_participant', 'ct9a1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct9a2'
        db.alter_column('eyevacs_participant', 'ct9a2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct9a3'
        db.alter_column('eyevacs_participant', 'ct9a3', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct16a4'
        db.alter_column('eyevacs_participant', 'ct16a4', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct11amount'
        db.alter_column('eyevacs_participant', 'ct11amount', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct15a2'
        db.alter_column('eyevacs_participant', 'ct15a2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct15a3'
        db.alter_column('eyevacs_participant', 'ct15a3', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct15a4'
        db.alter_column('eyevacs_participant', 'ct15a4', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.rnd_happinessQ4'
        db.alter_column('eyevacs_participant', 'rnd_happinessQ4', self.gf('django.db.models.fields.IntegerField')(max_length=100, null=True))

        # Changing field 'Participant.rnd_happinessQ2'
        db.alter_column('eyevacs_participant', 'rnd_happinessQ2', self.gf('django.db.models.fields.IntegerField')(max_length=100, null=True))

        # Changing field 'Participant.rnd_happinessQ3'
        db.alter_column('eyevacs_participant', 'rnd_happinessQ3', self.gf('django.db.models.fields.IntegerField')(max_length=100, null=True))

        # Changing field 'Participant.rnd_happinessQ1'
        db.alter_column('eyevacs_participant', 'rnd_happinessQ1', self.gf('django.db.models.fields.IntegerField')(max_length=100, null=True))

        # Changing field 'Participant.ctamount9'
        db.alter_column('eyevacs_participant', 'ctamount9', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct16amount'
        db.alter_column('eyevacs_participant', 'ct16amount', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct12a5'
        db.alter_column('eyevacs_participant', 'ct12a5', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct12a4'
        db.alter_column('eyevacs_participant', 'ct12a4', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct12a1'
        db.alter_column('eyevacs_participant', 'ct12a1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct12a3'
        db.alter_column('eyevacs_participant', 'ct12a3', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.rnd_happiness_order'
        db.alter_column('eyevacs_participant', 'rnd_happiness_order', self.gf('django.db.models.fields.TextField')(max_length=100, null=True))

        # Changing field 'Participant.ct10amount'
        db.alter_column('eyevacs_participant', 'ct10amount', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct14a2'
        db.alter_column('eyevacs_participant', 'ct14a2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct14amount'
        db.alter_column('eyevacs_participant', 'ct14amount', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct16'
        db.alter_column('eyevacs_participant', 'ct16', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct14'
        db.alter_column('eyevacs_participant', 'ct14', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct12'
        db.alter_column('eyevacs_participant', 'ct12', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct13'
        db.alter_column('eyevacs_participant', 'ct13', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct10'
        db.alter_column('eyevacs_participant', 'ct10', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct11'
        db.alter_column('eyevacs_participant', 'ct11', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct12a2'
        db.alter_column('eyevacs_participant', 'ct12a2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct16pk'
        db.alter_column('eyevacs_participant', 'ct16pk', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct16a2'
        db.alter_column('eyevacs_participant', 'ct16a2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct16a5'
        db.alter_column('eyevacs_participant', 'ct16a5', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct16a1'
        db.alter_column('eyevacs_participant', 'ct16a1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct15amount'
        db.alter_column('eyevacs_participant', 'ct15amount', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct12pk'
        db.alter_column('eyevacs_participant', 'ct12pk', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct15a1'
        db.alter_column('eyevacs_participant', 'ct15a1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct14pk'
        db.alter_column('eyevacs_participant', 'ct14pk', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct13a1'
        db.alter_column('eyevacs_participant', 'ct13a1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct13a2'
        db.alter_column('eyevacs_participant', 'ct13a2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct15'
        db.alter_column('eyevacs_participant', 'ct15', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct13a4'
        db.alter_column('eyevacs_participant', 'ct13a4', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct13a5'
        db.alter_column('eyevacs_participant', 'ct13a5', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct14a4'
        db.alter_column('eyevacs_participant', 'ct14a4', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct15a5'
        db.alter_column('eyevacs_participant', 'ct15a5', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct11a4'
        db.alter_column('eyevacs_participant', 'ct11a4', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.rnd_happiness_order_pk'
        db.alter_column('eyevacs_participant', 'rnd_happiness_order_pk', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct11pk'
        db.alter_column('eyevacs_participant', 'ct11pk', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct9amount'
        db.alter_column('eyevacs_participant', 'ct9amount', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct13a3'
        db.alter_column('eyevacs_participant', 'ct13a3', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct16a3'
        db.alter_column('eyevacs_participant', 'ct16a3', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ctamount14'
        db.alter_column('eyevacs_participant', 'ctamount14', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ctamount15'
        db.alter_column('eyevacs_participant', 'ctamount15', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ctamount16'
        db.alter_column('eyevacs_participant', 'ctamount16', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ctamount11'
        db.alter_column('eyevacs_participant', 'ctamount11', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct12amount'
        db.alter_column('eyevacs_participant', 'ct12amount', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ctamount10'
        db.alter_column('eyevacs_participant', 'ctamount10', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Participant.ct14a1'
        db.alter_column('eyevacs_participant', 'ct14a1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

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
            'h1conjoint1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'h1conjoint2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'h1conjoint3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'h1conjoint4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'h1conjoint5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'h1conjoint6': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'h1conjoint7': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'h1conjoint8': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'h2durationpath': ('django.db.models.fields.TextField', [], {}),
            'h2searchpath': ('django.db.models.fields.TextField', [], {}),
            'h2totaltime': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'h2transitdecision': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'hard_id': ('django.db.models.fields.IntegerField', [], {}),
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
            't_expl_distance': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_expl_fav': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_expl_food': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_expl_price': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_expl_recommend': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_expl_room': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_expl_view': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_h1page1': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_h1page2': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_h2transitdecision': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_rnd_happiness': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_rnd_involvement': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_rnd_max': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_rnd_regret': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            't_rnd_searchgoals': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '50'}),
            'testpcpt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'total_time': ('django.db.models.fields.CharField', [], {'default': "'9999'", 'max_length': '100'}),
            'validated_pretest': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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