from django.db import models

LANGUAGE_CHOICES = (
        ('de','Deutsch'),
        ('en','English'),
    )
GROUP_CHOICES = (
        ('inc','increasing'),
        ('dec','decreasing'),
        ('bsl','baseline'),

    )
GENDER_CHOICES = (
        ('m','Male'),
        ('f','Female'),
    )
EXT_DATA_TYPE = (
        ('ctask','Choice Task File'),
        ('bltsk','Base-Line Task File'),
        ('scale','Random Scale Ordering File'),
    )

class Experiment(models.Model):
    #grunddaten:
    # displayed_survey_values: are linked through foreign key in external data class
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=2, choices= LANGUAGE_CHOICES)
    #participants:wird als foreign key bei den participants geloest

class Participant(models.Model):
    #bool, real participant = 1 or "Test-Experiments" = 0 
    genuine = models.BooleanField()
    date = models.DateTimeField("date created")
    #inc, dec, bsl
    group = models.CharField(max_length=3, choices= GROUP_CHOICES)
    #2nd page: begin_radio.html
    begin_radio_recent = models.IntegerField()
    begin_radio_bool= models.IntegerField()
    begin_radio_quantity = models.IntegerField()
    begin_radio_searchdepth = models.IntegerField()
    #begin likert
    begin_likert_services = models.IntegerField()
    begin_likert_alikeness = models.IntegerField()
    begin_likert_importance = models.IntegerField()
    begin_likert_regret = models.IntegerField()
    #Array of Choice Tasks IDs, the number counts the chronological order of the decisions! Values: 0-23 (3*8), links to db_ct_id_{#}
    ct_id = models.CharField(max_length = (7*3+6)*3) #
    #final choice array
    ct_choice = models.CharField(max_length = 7+6) #5,4,7,2,4,2,...
    #not defined yet! links to external file... same structure as "ct"
    hc_id = models.CharField(max_length = 3*3+2)
    hc_choice = models.CharField(max_length = 3+2)
    #Picking a choice writes it to ts_list. They form the Tournament selection.
    ts_list = models.CharField(max_length = 7*(7+8)+6) #8+7 for an item, 7 total items, items are seperated by ';'
    #id of picked ts_list
    ts_choice = models.IntegerField() # 1 simple number, non randomized position in array
    #randomized order of the displayed ct's for the tournament selection
    ts_order = models.CharField(max_length = 7+6)
    #creation of a participant assigns him an individual randomization order of the max regret scale, links to external file: db_scale_rnd_id
    scale_rnd_id = models.IntegerField()
    #extracted order, less database dependence
    scale_rnd_order = models.CharField(max_length = 100)
    #array with ordered values of the max regret scale
    scale_max_regret = models.CharField(max_length = 100) #ca. 18*2 +17 felder 
    #array of choices in the heuristics scale, length: 6 
    heur_choice = models.CharField(max_length = 6+5)
    #demographics
    demo_gender = models.CharField(max_length=6, choices= GENDER_CHOICES)
    demo_student_bool = models.BooleanField()
    demo_semester = models.IntegerField()
    demo_age = models.IntegerField()
    #array of timestamp per finished page
    pg_time = models.CharField(max_length = 18*17+17) #323 with all values in ms since 1970-1-1 00:00:00 resulting in 17 digits per timestamp. 12 if milliseconds are omitted. 18*12+17  should be best!
    #order of pages displayed, writes id of each page to this array
    pg_order = models.CharField(max_length = 100)
        #experiment
    experiment = models.ForeignKey(Experiment)


class Attribute(models.Model):
    #is th
    name = models.CharField(max_length = 100)
    #experiment setup to which this attribute belongs to
    exp_setup = models.ForeignKey(Experiment)
    #position in external source file, values: 4-8
    position = models.SmallIntegerField()

class Level(models.Model):
    #quantity of alternatives 
    link_attribute = models.ForeignKey(Attribute)
    name = models.CharField(max_length = 100)
    #numerical value to represent the name of the level
    value = models.IntegerField()

class External_Source_Data(models.Model):
    # db_ct_id_{#}, db_rndorder_scale
    filetype = models.CharField(max_length =5, choices= EXT_DATA_TYPE)
    header = models.CharField(max_length = 100)
    exp_name = models.CharField(max_length = 100)
    experiment = models.ForeignKey(Experiment)

#class External_Data_Column(models.Model):
#    name = models.CharField(max_length = 100)
#    parent = models.ForeignKey(External_Source_Data)

class External_Choice_Task(models.Model):
    id_hard = models.CharField(max_length = 100) #Source Document ID, not DjangoPK
    ext_src_data = models.ForeignKey(External_Source_Data)
    ext_src_data_name = models.CharField(max_length = 100)
    amount = models.IntegerField()
    a1 = models.CharField(max_length = 15, default = "empty")
    a2 = models.CharField(max_length = 15, default = "empty")
    a3 = models.CharField(max_length = 15, default = "empty")
    a4 = models.CharField(max_length = 15, default = "empty")
    a5 = models.CharField(max_length = 15, default = "empty")
    a6 = models.CharField(max_length = 15, default = "empty")
    a7 = models.CharField(max_length = 15, default = "empty")
    a8 = models.CharField(max_length = 15, default = "empty")
    used = models.BooleanField()
    linked_pcpt = models.ForeignKey(Participant, null = True, blank = True)
    raw_src_line = models.CharField(max_length = 100)

class External_Baseline_Choice_Task(models.Model):
    #identifies a 'Baseline Participant!
    id_hard = models.CharField(max_length = 100) #Source Document ID, not DjangoPK
    #Source ID Task Number, currently max value = 21 (3*7)
    task = models.IntegerField()
    ext_src_data = models.ForeignKey(External_Source_Data)
    ext_src_data_name = models.CharField(max_length = 100)
    #amount is not needed, 5 Alternatives is hardcoded.
    a1 = models.CharField(max_length = 15, default = "empty")
    a2 = models.CharField(max_length = 15, default = "empty")
    a3 = models.CharField(max_length = 15, default = "empty")
    a4 = models.CharField(max_length = 15, default = "empty")
    a5 = models.CharField(max_length = 15, default = "empty")
    used = models.BooleanField()
    linked_pcpt = models.ForeignKey(Participant, null = True, blank = True)
    raw_src_line = models.CharField(max_length = 100)

class External_Order_Scale(models.Model):
    id_hard = models.CharField(max_length = 100)
    scale_rnd_order_ext = models.CharField(max_length = 100)
    linked_pcpt = models.ForeignKey(Participant, null = True, blank = True)

