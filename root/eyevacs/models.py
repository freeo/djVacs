from django.db import models
from datetime import datetime

LANGUAGE_CHOICES = (
        ('de','Deutsch'),
        ('en','English'),
    )
GROUP_CHOICES = (
        ('inc','increasing'),
        ('dec','decreasing'),
        ('bl1','baseline'),
        ('bl2','baseline2'),
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
    info = models.TextField( blank = True)
    #participants:wird als foreign key bei den participants geloest

# class PubContainer(models.Model):
    # experiment = models.ForeignKey(Experiment)

class Pub(models.Model):
    # container = models.ForeignKey(PubContainer)
    experiment = models.ForeignKey(Experiment)
    # set: scale_order_ids
    #used as a dictionary of this pubs scale orderings
    #Foreign Keys:
    #external_order_scale

    sessionid = models.CharField(max_length = 150)
    csrftoken = models.CharField(max_length = 150)

    ct_size = models.IntegerField()
    # index of grouping.group_nr[index]
    hard_id = models.IntegerField()
    def_group = models.IntegerField()
    #manual ID used?
    #if overridde_id == false: man_group = None
    override_group= models.IntegerField( null = True, blank = True)
    create_time = models.DateTimeField(default = datetime.now, blank = True)


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
    header = models.CharField(max_length = 200)
    exp_name = models.CharField(max_length = 100)
    experiment = models.ForeignKey(Experiment)
    info = models.TextField( blank = True)
    range_start = models.IntegerField(default=0)
    range_end = models.IntegerField(null = True, blank = True)

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
    linked_pcpt = models.ForeignKey('eyevacs.Participant', null = True, blank = True, related_name = 'Choice_TasksAsParticipant')
    linked_pub = models.ForeignKey(Pub, null = True, blank = True, related_name = 'Choice_TasksAsPub')
    raw_src_line = models.CharField(max_length = 100)

class External_Baseline_Choice_Task(models.Model):
    #identifies a 'Baseline Participant!
    id_hard = models.CharField(max_length = 100) #Source Document ID, not DjangoPK
    #Source ID Task Number, currently max value = 21 (3*7)
    task = models.IntegerField()
    ext_src_data = models.ForeignKey(External_Source_Data)
    ext_src_data_name = models.CharField(max_length = 100)
    #amount is not needed, 5 Alternatives is hardcoded.
    #amount is needed now. 2 bsl groups make it necessary
    amount = models.IntegerField()
    a1 = models.CharField(max_length = 15, default = "empty")
    a2 = models.CharField(max_length = 15, default = "empty")
    a3 = models.CharField(max_length = 15, default = "empty")
    a4 = models.CharField(max_length = 15, default = "empty")
    a5 = models.CharField(max_length = 15, default = "empty")
    used = models.BooleanField()
    linked_pcpt = models.ForeignKey('eyevacs.Participant', null = True, blank = True, related_name = 'Baseline_Choice_TasksAsParticipant')
    linked_pub = models.ForeignKey(Pub, null = True, blank = True, related_name = 'Baseline_Choice_TasksAsPub')
    raw_src_line = models.CharField(max_length = 100)

class External_Order_Scale(models.Model):
    id_hard = models.CharField(max_length = 100)
    scale_rnd_order_ext = models.CharField(max_length = 100)
    source_file = models.ForeignKey(External_Source_Data, null = True, blank = True)
    linked_pcpt = models.ForeignKey('eyevacs.Participant', null = True, blank = True)
    linked_pub = models.ForeignKey(Pub, null = True, blank = True)
    used = models.BooleanField()

class Scale(models.Model):
    name = models.CharField(max_length = 100)
    experiment = models.ForeignKey(Experiment)
    rnd_file = models.OneToOneField(External_Source_Data, primary_key=True)

class Scale_Question(models.Model):
    linked_scale = models.ForeignKey(Scale)
    text = models.TextField()
    #initial order of the question!
    id_order = models.IntegerField()

class Grouping(models.Model):
    experiment = models.OneToOneField(Experiment)
    seed = models.IntegerField()
    counter = models.IntegerField()
    #JSON-serialized (text) version of group numberlist
    group_nr = models.TextField( null=True)
    # sharingpoint = models.IntegerField(default=0)
    # JSON field
    id_holes = models.TextField( null=True)
    id_hole_history = models.TextField( null=True)


class Participant(models.Model):
    experiment = models.ForeignKey(Experiment)
    #is unique per exp, not more. grouping.group_nr[hard_id] sets condition
    hard_id = models.IntegerField()
    #inc, dec, bsl
    def_group = models.CharField(max_length=3, choices= GROUP_CHOICES)
    override_group= models.CharField(max_length=3, null = True, blank = True, choices = GROUP_CHOICES)
    ct_size = models.IntegerField()
    #bool, real participant = False or "Test-Experiments" = True
    #maybe a switch in admin mask
    testpcpt = models.BooleanField()
    validated_pretest = models.BooleanField(default= False)
    # begin time is pubs create_time
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField(default = datetime.now, blank = True)
    total_time = models.CharField(max_length=100, default='9999')
    rnd_maxQ1 = models.CharField(max_length=100)
    rnd_maxQ2 = models.CharField(max_length=100)
    rnd_maxQ3 = models.CharField(max_length=100)
    rnd_maxQ4 = models.CharField(max_length=100)
    rnd_maxQ5 = models.CharField(max_length=100)
    rnd_maxQ6 = models.CharField(max_length=100)
    t_rnd_max = models.CharField(max_length=50, default='9999')
    rnd_regretQ1 = models.CharField(max_length=100)
    rnd_regretQ2 = models.CharField(max_length=100)
    rnd_regretQ3 = models.CharField(max_length=100)
    rnd_regretQ4 = models.CharField(max_length=100)
    rnd_regretQ5 = models.CharField(max_length=100)
    t_rnd_regret = models.CharField(max_length=50, default='9999')
    experience_lastvacation = models.CharField(max_length=100)
    experience_planningvacation = models.CharField(max_length=100)
    experience_searchduration = models.CharField(max_length=100)
    t_experience = models.CharField(max_length=50, default='9999')
    rnd_involvementQ1 = models.CharField(max_length=100)
    rnd_involvementQ2 = models.CharField(max_length=100)
    rnd_involvementQ3 = models.CharField(max_length=100)
    rnd_involvementQ4 = models.CharField(max_length=100)
    t_rnd_involvement = models.CharField(max_length=50, default='9999')

    explanation_distance = models.CharField(max_length=100)
    t_expl_distance = models.CharField(max_length=50, default='9999')
    explanation_food = models.CharField(max_length=100)
    t_expl_food = models.CharField(max_length=50, default='9999')
    explanation_price = models.CharField(max_length=100)
    t_expl_price = models.CharField(max_length=50, default='9999')
    explanation_recommend = models.CharField(max_length=100)
    t_expl_recommend = models.CharField(max_length=50, default='9999')
    explanation_room = models.CharField(max_length=100)
    t_expl_room = models.CharField(max_length=50, default='9999')
    explanation_view = models.CharField(max_length=100)
    t_expl_view = models.CharField(max_length=50, default='9999')
    fav_distance = models.CharField(max_length=100)
    fav_food = models.CharField(max_length=100)
    fav_price = models.CharField(max_length=100)
    fav_recommending = models.CharField(max_length=100)
    fav_room = models.CharField(max_length=100)
    fav_seaview = models.CharField(max_length=100)
    t_expl_fav = models.CharField(max_length=50, default='9999')
    #the final decision
    ct1 = models.CharField(max_length=100)
    ct2 = models.CharField(max_length=100)
    ct3 = models.CharField(max_length=100)
    ct4 = models.CharField(max_length=100)
    ct5 = models.CharField(max_length=100)
    ct6 = models.CharField(max_length=100)
    ct7 = models.CharField(max_length=100)
    ct8 = models.CharField(max_length=100)
    ct9 = models.CharField(max_length=100, null = True, blank = True)
    ct10 = models.CharField(max_length=100, null = True, blank = True)
    ct11 = models.CharField(max_length=100, null = True, blank = True)
    ct12 = models.CharField(max_length=100, null = True, blank = True)
    ct13 = models.CharField(max_length=100, null = True, blank = True)
    ct14 = models.CharField(max_length=100, null = True, blank = True)
    ct15 = models.CharField(max_length=100, null = True, blank = True)
    ct16 = models.CharField(max_length=100, null = True, blank = True)
    #amount of alternatives presented
    #kind of redundant, yet VERY helpful!
    ctamount1 = models.CharField(max_length=100)
    ctamount2 = models.CharField(max_length=100)
    ctamount3 = models.CharField(max_length=100)
    ctamount4 = models.CharField(max_length=100)
    ctamount5 = models.CharField(max_length=100)
    ctamount6 = models.CharField(max_length=100)
    ctamount7 = models.CharField(max_length=100)
    ctamount8 = models.CharField(max_length=100)
    ctamount9 = models.CharField(max_length=100, null = True, blank = True)
    ctamount10 = models.CharField(max_length=100, null = True, blank = True)
    ctamount11 = models.CharField(max_length=100, null = True, blank = True)
    ctamount12 = models.CharField(max_length=100, null = True, blank = True)
    ctamount13 = models.CharField(max_length=100, null = True, blank = True)
    ctamount14 = models.CharField(max_length=100, null = True, blank = True)
    ctamount15 = models.CharField(max_length=100, null = True, blank = True)
    ctamount16 = models.CharField(max_length=100, null = True, blank = True)
    cttime1 = models.CharField(max_length=100)
    cttime2 = models.CharField(max_length=100)
    cttime3 = models.CharField(max_length=100)
    cttime4 = models.CharField(max_length=100)
    cttime5 = models.CharField(max_length=100)
    cttime6 = models.CharField(max_length=100)
    cttime7 = models.CharField(max_length=100)
    cttime8 = models.CharField(max_length=100)
    cttime9 = models.CharField(max_length=100, null = True, blank = True)
    cttime10 = models.CharField(max_length=100, null = True, blank = True)
    cttime11 = models.CharField(max_length=100, null = True, blank = True)
    cttime12 = models.CharField(max_length=100, null = True, blank = True)
    cttime13 = models.CharField(max_length=100, null = True, blank = True)
    cttime14 = models.CharField(max_length=100, null = True, blank = True)
    cttime15 = models.CharField(max_length=100, null = True, blank = True)
    cttime16 = models.CharField(max_length=100, null = True, blank = True)
    h1conjoint1 = models.CharField(max_length=100)
    h1conjoint2 = models.CharField(max_length=100)
    h1conjoint3 = models.CharField(max_length=100)
    h1conjoint4 = models.CharField(max_length=100)
    t_h1page1 = models.CharField(max_length=50, default='9999')
    h1conjoint5 = models.CharField(max_length=100)
    h1conjoint6 = models.CharField(max_length=100)
    h1conjoint7 = models.CharField(max_length=100)
    h1conjoint8 = models.CharField(max_length=100)
    t_h1page2 = models.CharField(max_length=50, default='9999')

    h2totaltime = models.CharField(max_length=100)
    h2searchpath = models.TextField()
    h2durationpath = models.TextField()
    h2transitdecision = models.CharField(max_length=100)
    t_h2transitdecision = models.CharField(max_length=50, default='9999')

    rnd_searchgoalsQ1 = models.IntegerField()
    rnd_searchgoalsQ2 = models.IntegerField()
    rnd_searchgoalsQ3 = models.IntegerField()
    rnd_searchgoalsQ4 = models.IntegerField()
    t_rnd_searchgoals = models.CharField(max_length=50, default='9999')
    #OPTIONAL EXPORT
    rnd_happinessQ1 = models.IntegerField(max_length=100, null = True, blank = True)
    rnd_happinessQ2 = models.IntegerField(max_length=100, null = True, blank = True)
    rnd_happinessQ3 = models.IntegerField(max_length=100, null = True, blank = True)
    rnd_happinessQ4 = models.IntegerField(max_length=100, null = True, blank = True)
    t_rnd_happiness = models.CharField(max_length=50, default='9999')

    demo_gender = models.CharField(max_length=6, choices= GENDER_CHOICES)
    demo_age = models.IntegerField()
    t_demographics = models.CharField(max_length=50, default='9999')

    #2nd seperate file on export
    #used initial pub data:
    raw_timestamps = models.TextField() #str(dict)

    ct1pk = models.CharField(max_length=100)
    ct1amount = models.CharField(max_length=100)
    ct1a1 = models.CharField(max_length=100)
    ct1a2 = models.CharField(max_length=100)
    ct1a3 = models.CharField(max_length=100)
    ct1a4 = models.CharField(max_length=100)
    ct1a5 = models.CharField(max_length=100)
    ct2pk = models.CharField(max_length=100)
    ct2amount = models.CharField(max_length=100)
    ct2a1 = models.CharField(max_length=100)
    ct2a2 = models.CharField(max_length=100)
    ct2a3 = models.CharField(max_length=100)
    ct2a4 = models.CharField(max_length=100)
    ct2a5 = models.CharField(max_length=100)
    ct3pk = models.CharField(max_length=100)
    ct3amount = models.CharField(max_length=100)
    ct3a1 = models.CharField(max_length=100)
    ct3a2 = models.CharField(max_length=100)
    ct3a3 = models.CharField(max_length=100)
    ct3a4 = models.CharField(max_length=100)
    ct3a5 = models.CharField(max_length=100)
    ct4pk = models.CharField(max_length=100)
    ct4amount = models.CharField(max_length=100)
    ct4a1 = models.CharField(max_length=100)
    ct4a2 = models.CharField(max_length=100)
    ct4a3 = models.CharField(max_length=100)
    ct4a4 = models.CharField(max_length=100)
    ct4a5 = models.CharField(max_length=100)
    ct5pk = models.CharField(max_length=100)
    ct5amount = models.CharField(max_length=100)
    ct5a1 = models.CharField(max_length=100)
    ct5a2 = models.CharField(max_length=100)
    ct5a3 = models.CharField(max_length=100)
    ct5a4 = models.CharField(max_length=100)
    ct5a5 = models.CharField(max_length=100)
    ct6pk = models.CharField(max_length=100)
    ct6amount = models.CharField(max_length=100)
    ct6a1 = models.CharField(max_length=100)
    ct6a2 = models.CharField(max_length=100)
    ct6a3 = models.CharField(max_length=100)
    ct6a4 = models.CharField(max_length=100)
    ct6a5 = models.CharField(max_length=100)
    ct7pk = models.CharField(max_length=100)
    ct7amount = models.CharField(max_length=100)
    ct7a1 = models.CharField(max_length=100)
    ct7a2 = models.CharField(max_length=100)
    ct7a3 = models.CharField(max_length=100)
    ct7a4 = models.CharField(max_length=100)
    ct7a5 = models.CharField(max_length=100)
    ct8pk = models.CharField(max_length=100)
    ct8amount = models.CharField(max_length=100)
    ct8a1 = models.CharField(max_length=100)
    ct8a2 = models.CharField(max_length=100)
    ct8a3 = models.CharField(max_length=100)
    ct8a4 = models.CharField(max_length=100)
    ct8a5 = models.CharField(max_length=100)
    #optional CTs
    ct9pk = models.CharField(max_length=100, null = True, blank = True)
    ct9amount = models.CharField(max_length=100, null = True, blank = True)
    ct9a1 = models.CharField(max_length=100, null = True, blank = True)
    ct9a2 = models.CharField(max_length=100, null = True, blank = True)
    ct9a3 = models.CharField(max_length=100, null = True, blank = True)
    ct9a4 = models.CharField(max_length=100, null = True, blank = True)
    ct9a5 = models.CharField(max_length=100, null = True, blank = True)
    ct10pk = models.CharField(max_length=100, null = True, blank = True)
    ct10amount = models.CharField(max_length=100, null = True, blank = True)
    ct10a1 = models.CharField(max_length=100, null = True, blank = True)
    ct10a2 = models.CharField(max_length=100, null = True, blank = True)
    ct10a3 = models.CharField(max_length=100, null = True, blank = True)
    ct10a4 = models.CharField(max_length=100, null = True, blank = True)
    ct10a5 = models.CharField(max_length=100, null = True, blank = True)
    ct11pk = models.CharField(max_length=100, null = True, blank = True)
    ct11amount = models.CharField(max_length=100, null = True, blank = True)
    ct11a1 = models.CharField(max_length=100, null = True, blank = True)
    ct11a2 = models.CharField(max_length=100, null = True, blank = True)
    ct11a3 = models.CharField(max_length=100, null = True, blank = True)
    ct11a4 = models.CharField(max_length=100, null = True, blank = True)
    ct11a5 = models.CharField(max_length=100, null = True, blank = True)
    ct12pk = models.CharField(max_length=100, null = True, blank = True)
    ct12amount = models.CharField(max_length=100, null = True, blank = True)
    ct12a1 = models.CharField(max_length=100, null = True, blank = True)
    ct12a2 = models.CharField(max_length=100, null = True, blank = True)
    ct12a3 = models.CharField(max_length=100, null = True, blank = True)
    ct12a4 = models.CharField(max_length=100, null = True, blank = True)
    ct12a5 = models.CharField(max_length=100, null = True, blank = True)
    ct13pk = models.CharField(max_length=100, null = True, blank = True)
    ct13amount = models.CharField(max_length=100, null = True, blank = True)
    ct13a1 = models.CharField(max_length=100, null = True, blank = True)
    ct13a2 = models.CharField(max_length=100, null = True, blank = True)
    ct13a3 = models.CharField(max_length=100, null = True, blank = True)
    ct13a4 = models.CharField(max_length=100, null = True, blank = True)
    ct13a5 = models.CharField(max_length=100, null = True, blank = True)
    ct14pk = models.CharField(max_length=100, null = True, blank = True)
    ct14amount = models.CharField(max_length=100, null = True, blank = True)
    ct14a1 = models.CharField(max_length=100, null = True, blank = True)
    ct14a2 = models.CharField(max_length=100, null = True, blank = True)
    ct14a3 = models.CharField(max_length=100, null = True, blank = True)
    ct14a4 = models.CharField(max_length=100, null = True, blank = True)
    ct14a5 = models.CharField(max_length=100, null = True, blank = True)
    ct15pk = models.CharField(max_length=100, null = True, blank = True)
    ct15amount = models.CharField(max_length=100, null = True, blank = True)
    ct15a1 = models.CharField(max_length=100, null = True, blank = True)
    ct15a2 = models.CharField(max_length=100, null = True, blank = True)
    ct15a3 = models.CharField(max_length=100, null = True, blank = True)
    ct15a4 = models.CharField(max_length=100, null = True, blank = True)
    ct15a5 = models.CharField(max_length=100, null = True, blank = True)
    ct16pk = models.CharField(max_length=100, null = True, blank = True)
    ct16amount = models.CharField(max_length=100, null = True, blank = True)
    ct16a1 = models.CharField(max_length=100, null = True, blank = True)
    ct16a2 = models.CharField(max_length=100, null = True, blank = True)
    ct16a3 = models.CharField(max_length=100, null = True, blank = True)
    ct16a4 = models.CharField(max_length=100, null = True, blank = True)
    ct16a5 = models.CharField(max_length=100, null = True, blank = True)

    #actual orders are added up json fields to save columns
    #index: question number - Value: position
    rnd_max_order_pk = models.CharField(max_length=100)
    rnd_max_order = models.TextField()
    rnd_regret_order_pk = models.CharField(max_length=100)
    rnd_regret_order = models.TextField()
    rnd_involvement_order_pk = models.CharField(max_length=100)
    rnd_involvement_order = models.TextField()
    rnd_searchgoals_order_pk = models.CharField(max_length=100)
    rnd_searchgoals_order = models.TextField()
    rnd_happiness_order_pk = models.CharField(max_length=100, null = True, blank = True)
    rnd_happiness_order = models.TextField(max_length=100, null = True, blank = True)

    raw_timestamps = models.TextField(default = 'not assigned')

