# from eyevacs import Participant
header = [ 'hard_id', 'def_group', 'override_group', 'ct_size', 'testpcpt',
    'valid_pcpt', 'begin_time', 'end_time', 'total_time', 't_welcome',
    'rnd_maxQ1', 'rnd_maxQ2', 'rnd_maxQ3', 'rnd_maxQ4', 'rnd_maxQ5', 'rnd_maxQ6', 't_rnd_max',
    'rnd_regretQ1', 'rnd_regretQ2', 'rnd_regretQ3', 'rnd_regretQ4', 'rnd_regretQ5', 't_rnd_regret',
    'experience_lastvacation    ', 'experience_planningvacation', 'experience_searchduration   ', 't_experience',
    'rnd_involvementQ1', 'rnd_involvementQ2', 'rnd_involvementQ3', 'rnd_involvementQ4', 't_rnd_involvement',
    't_expl_0_overview', 'explanation_food', 't_expl_1_food', 'explanation_recommend', 't_expl_2_recommend', 'explanation_distance', 't_expl_3_distance', 'explanation_view', 't_expl_4_view', 'explanation_price', 't_expl_5_price', 'explanation_room', 't_expl_6_room',
    'fav_food', 'fav_recommending', 'fav_distance', 'fav_seaview', 'fav_price', 'fav_room', 't_expl_7_fav', 't_expl_8_ctseqintro',
    'ct1', 'ct2', 'ct3', 'ct4', 'ct5', 'ct6', 'ct7', 'ct8', 'ct9  ', 'ct10', 'ct11', 'ct12', 'ct13', 'ct14', 'ct15', 'ct16',
    'ctamount1', 'ctamount2', 'ctamount3', 'ctamount4', 'ctamount5', 'ctamount6', 'ctamount7', 'ctamount8', 'ctamount9  ', 'ctamount10', 'ctamount11', 'ctamount12', 'ctamount13', 'ctamount14', 'ctamount15', 'ctamount16',
    'cttime1', 'cttime2', 'cttime3', 'cttime4', 'cttime5', 'cttime6', 'cttime7', 'cttime8', 'cttime9', 'cttime10', 'cttime11', 'cttime12', 'cttime13', 'cttime14', 'cttime15', 'cttime16',
    'h1conjoint1', 'h1conjoint2', 'h1conjoint3', 'h1conjoint4', 't_h1page1', 't_loadingconjoint',
    'h1conjoint5', 'h1conjoint6', 'h1conjoint7', 'h1conjoint8', 't_h1page2',
    'h2totaltime', 'h2searchpath', 'h2durationpath', 'h2transitdecision', 't_h2transitdecision',
    'rnd_searchgoalsQ1', 'rnd_searchgoalsQ2', 'rnd_searchgoalsQ3', 'rnd_searchgoalsQ4', 't_rnd_searchgoals',
    'rnd_happinessQ1', 'rnd_happinessQ2', 'rnd_happinessQ3', 'rnd_happinessQ4', 't_rnd_happiness',
    'demo_gender', 'demo_age', 't_demographics',
    'ct1pk', 'ct1amount', 'ct1a1', 'ct1a2', 'ct1a3', 'ct1a4', 'ct1a5',
    'ct2pk', 'ct2amount', 'ct2a1', 'ct2a2', 'ct2a3', 'ct2a4', 'ct2a5',
    'ct3pk', 'ct3amount', 'ct3a1', 'ct3a2', 'ct3a3', 'ct3a4', 'ct3a5',
    'ct4pk', 'ct4amount', 'ct4a1', 'ct4a2', 'ct4a3', 'ct4a4', 'ct4a5',
    'ct5pk', 'ct5amount', 'ct5a1', 'ct5a2', 'ct5a3', 'ct5a4', 'ct5a5',
    'ct6pk', 'ct6amount', 'ct6a1', 'ct6a2', 'ct6a3', 'ct6a4', 'ct6a5',
    'ct7pk', 'ct7amount', 'ct7a1', 'ct7a2', 'ct7a3', 'ct7a4', 'ct7a5',
    'ct8pk', 'ct8amount', 'ct8a1', 'ct8a2', 'ct8a3', 'ct8a4', 'ct8a5',
    'ct9pk', 'ct9amount', 'ct9a1', 'ct9a2', 'ct9a3', 'ct9a4', 'ct9a5',
    'ct10pk', 'ct10amount', 'ct10a1', 'ct10a2', 'ct10a3', 'ct10a4', 'ct10a5',
    'ct11pk', 'ct11amount', 'ct11a1', 'ct11a2', 'ct11a3', 'ct11a4', 'ct11a5',
    'ct12pk', 'ct12amount', 'ct12a1', 'ct12a2', 'ct12a3', 'ct12a4', 'ct12a5',
    'ct13pk', 'ct13amount', 'ct13a1', 'ct13a2', 'ct13a3', 'ct13a4', 'ct13a5',
    'ct14pk', 'ct14amount', 'ct14a1', 'ct14a2', 'ct14a3', 'ct14a4', 'ct14a5',
    'ct15pk', 'ct15amount', 'ct15a1', 'ct15a2', 'ct15a3', 'ct15a4', 'ct15a5',
    'ct16pk', 'ct16amount', 'ct16a1', 'ct16a2', 'ct16a3', 'ct16a4', 'ct16a5',
    'rnd_max_order_pk', 'rnd_max_order', 'rnd_regret_order_pk', 'rnd_regret_order', 'rnd_involvement_order_pk', 'rnd_involvement_order', 'rnd_searchgoals_order_pk', 'rnd_searchgoals_order', 'rnd_happiness_order_pk', 'rnd_happiness_order',
    'raw_timestamps']

def pcpt_export_sequence(PCPT):
    export_sequence = [PCPT.hard_id,
        PCPT.def_group,
        PCPT.override_group,
        PCPT.ct_size,
        PCPT.testpcpt,
        PCPT.valid_pcpt  ,
        PCPT.begin_time,
        PCPT.end_time,
        PCPT.total_time,
        PCPT.t_welcome,
        PCPT.rnd_maxQ1,
        PCPT.rnd_maxQ2,
        PCPT.rnd_maxQ3,
        PCPT.rnd_maxQ4,
        PCPT.rnd_maxQ5,
        PCPT.rnd_maxQ6,
        PCPT.t_rnd_max,
        PCPT.rnd_regretQ1,
        PCPT.rnd_regretQ2,
        PCPT.rnd_regretQ3,
        PCPT.rnd_regretQ4,
        PCPT.rnd_regretQ5,
        PCPT.t_rnd_regret,
        PCPT.experience_lastvacation,
        PCPT.experience_planningvacation,
        PCPT.experience_searchduration,
        PCPT.t_experience,
        PCPT.rnd_involvementQ1,
        PCPT.rnd_involvementQ2,
        PCPT.rnd_involvementQ3,
        PCPT.rnd_involvementQ4,
        PCPT.t_rnd_involvement,
        PCPT.t_expl_0_overview,
        PCPT.explanation_food ,
        PCPT.t_expl_1_food ,
        PCPT.explanation_recommend ,
        PCPT.t_expl_2_recommend ,
        PCPT.explanation_distance ,
        PCPT.t_expl_3_distance ,
        PCPT.explanation_view ,
        PCPT.t_expl_4_view ,
        PCPT.explanation_price ,
        PCPT.t_expl_5_price ,
        PCPT.explanation_room ,
        PCPT.t_expl_6_room ,
        PCPT.fav_food ,
        PCPT.fav_recommending ,
        PCPT.fav_distance ,
        PCPT.fav_seaview ,
        PCPT.fav_price ,
        PCPT.fav_room ,
        PCPT.t_expl_7_fav ,
        PCPT.t_expl_8_ctseqintro ,
        PCPT.ct1,
        PCPT.ct2,
        PCPT.ct3,
        PCPT.ct4,
        PCPT.ct5,
        PCPT.ct6,
        PCPT.ct7,
        PCPT.ct8,
        PCPT.ct9,
        PCPT.ct10,
        PCPT.ct11,
        PCPT.ct12,
        PCPT.ct13,
        PCPT.ct14,
        PCPT.ct15,
        PCPT.ct16,
        PCPT.ctamount1,
        PCPT.ctamount2,
        PCPT.ctamount3,
        PCPT.ctamount4,
        PCPT.ctamount5,
        PCPT.ctamount6,
        PCPT.ctamount7,
        PCPT.ctamount8,
        PCPT.ctamount9,
        PCPT.ctamount10,
        PCPT.ctamount11,
        PCPT.ctamount12,
        PCPT.ctamount13,
        PCPT.ctamount14,
        PCPT.ctamount15,
        PCPT.ctamount16,
        PCPT.cttime1,
        PCPT.cttime2,
        PCPT.cttime3,
        PCPT.cttime4,
        PCPT.cttime5,
        PCPT.cttime6,
        PCPT.cttime7,
        PCPT.cttime8,
        PCPT.cttime9,
        PCPT.cttime10,
        PCPT.cttime11,
        PCPT.cttime12,
        PCPT.cttime13,
        PCPT.cttime14,
        PCPT.cttime15,
        PCPT.cttime16,
        PCPT.h1conjoint1,
        PCPT.h1conjoint2,
        PCPT.h1conjoint3,
        PCPT.h1conjoint4,
        PCPT.t_h1page1,
        PCPT.t_loadingconjoint,
        PCPT.h1conjoint5,
        PCPT.h1conjoint6,
        PCPT.h1conjoint7,
        PCPT.h1conjoint8,
        PCPT.t_h1page2,
        PCPT.h2totaltime,
        PCPT.h2searchpath,
        PCPT.h2durationpath,
        PCPT.h2transitdecision,
        PCPT.t_h2transitdecision,
        PCPT.rnd_searchgoalsQ1,
        PCPT.rnd_searchgoalsQ2,
        PCPT.rnd_searchgoalsQ3,
        PCPT.rnd_searchgoalsQ4,
        PCPT.t_rnd_searchgoals,
        PCPT.rnd_happinessQ1,
        PCPT.rnd_happinessQ2,
        PCPT.rnd_happinessQ3,
        PCPT.rnd_happinessQ4,
        PCPT.t_rnd_happiness,
        PCPT.demo_gender,
        PCPT.demo_age,
        PCPT.t_demographics,
        PCPT.ct1pk,
        PCPT.ct1amount,
        PCPT.ct1a1,
        PCPT.ct1a2,
        PCPT.ct1a3,
        PCPT.ct1a4,
        PCPT.ct1a5,
        PCPT.ct2pk,
        PCPT.ct2amount,
        PCPT.ct2a1,
        PCPT.ct2a2,
        PCPT.ct2a3,
        PCPT.ct2a4,
        PCPT.ct2a5,
        PCPT.ct3pk,
        PCPT.ct3amount,
        PCPT.ct3a1,
        PCPT.ct3a2,
        PCPT.ct3a3,
        PCPT.ct3a4,
        PCPT.ct3a5,
        PCPT.ct4pk,
        PCPT.ct4amount,
        PCPT.ct4a1,
        PCPT.ct4a2,
        PCPT.ct4a3,
        PCPT.ct4a4,
        PCPT.ct4a5,
        PCPT.ct5pk,
        PCPT.ct5amount,
        PCPT.ct5a1,
        PCPT.ct5a2,
        PCPT.ct5a3,
        PCPT.ct5a4,
        PCPT.ct5a5,
        PCPT.ct6pk,
        PCPT.ct6amount,
        PCPT.ct6a1,
        PCPT.ct6a2,
        PCPT.ct6a3,
        PCPT.ct6a4,
        PCPT.ct6a5,
        PCPT.ct7pk,
        PCPT.ct7amount,
        PCPT.ct7a1,
        PCPT.ct7a2,
        PCPT.ct7a3,
        PCPT.ct7a4,
        PCPT.ct7a5,
        PCPT.ct8pk,
        PCPT.ct8amount,
        PCPT.ct8a1,
        PCPT.ct8a2,
        PCPT.ct8a3,
        PCPT.ct8a4,
        PCPT.ct8a5,
        PCPT.ct9pk,
        PCPT.ct9amount,
        PCPT.ct9a1,
        PCPT.ct9a2,
        PCPT.ct9a3,
        PCPT.ct9a4,
        PCPT.ct9a5,
        PCPT.ct10pk,
        PCPT.ct10amount,
        PCPT.ct10a1,
        PCPT.ct10a2,
        PCPT.ct10a3,
        PCPT.ct10a4,
        PCPT.ct10a5,
        PCPT.ct11pk,
        PCPT.ct11amount,
        PCPT.ct11a1,
        PCPT.ct11a2,
        PCPT.ct11a3,
        PCPT.ct11a4,
        PCPT.ct11a5,
        PCPT.ct12pk,
        PCPT.ct12amount,
        PCPT.ct12a1,
        PCPT.ct12a2,
        PCPT.ct12a3,
        PCPT.ct12a4,
        PCPT.ct12a5,
        PCPT.ct13pk,
        PCPT.ct13amount,
        PCPT.ct13a1,
        PCPT.ct13a2,
        PCPT.ct13a3,
        PCPT.ct13a4,
        PCPT.ct13a5,
        PCPT.ct14pk,
        PCPT.ct14amount,
        PCPT.ct14a1,
        PCPT.ct14a2,
        PCPT.ct14a3,
        PCPT.ct14a4,
        PCPT.ct14a5,
        PCPT.ct15pk,
        PCPT.ct15amount,
        PCPT.ct15a1,
        PCPT.ct15a2,
        PCPT.ct15a3,
        PCPT.ct15a4,
        PCPT.ct15a5,
        PCPT.ct16pk,
        PCPT.ct16amount,
        PCPT.ct16a1,
        PCPT.ct16a2,
        PCPT.ct16a3,
        PCPT.ct16a4,
        PCPT.ct16a5,
        PCPT.rnd_max_order_pk,
        PCPT.rnd_max_order,
        PCPT.rnd_regret_order_pk,
        PCPT.rnd_regret_order,
        PCPT.rnd_involvement_order_pk,
        PCPT.rnd_involvement_order,
        PCPT.rnd_searchgoals_order_pk,
        PCPT.rnd_searchgoals_order,
        PCPT.rnd_happiness_order_pk,
        PCPT.rnd_happiness_order,
        PCPT.raw_timestamps]
    return export_sequence
