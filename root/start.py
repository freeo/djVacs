import os
import sys
import re
import random
from scripts import load_fixtures, create_fixtures, create_rnd_scale, scale_questions, grouping, load_setup
from subprocess import call
from eyevacs.models import Experiment, External_Source_Data, External_Choice_Task, External_Order_Scale, External_Baseline_Choice_Task, Scale, Scale_Question, Grouping, Attribute, Level, Participant, Pub
from django.db import transaction
from django.db.models import Max
from django.forms.models import model_to_dict

#paths
root = '' #sys.path[0]
external_data_path = './external_data/'
fixture_output = './eyevacs/fixtures/'
output_data_path = './eyevacs/'
experiment_name = ''
exp_filename = ''
current_exp_id = None
use_def_scales = True
default_scales = [('Max',1,6),('Regret',1,5),('Involvement',1,4),('SearchGoals',1,4),('Happiness',1,4)]



def SetExperimentDjangoPK():
    '''Gets a free personal key identifier for the new current Experiment Model.'''

    exp_count = Experiment.objects.count()
    return exp_count + 1

def MakeExperiment(name, language):
    '''Create an Experiment Model Fixture.'''

    single_model = r'{"model":"%s","pk":%s,"fields":{%s}}'
    output = "[%s]"
    existing_experiments = Experiment.objects.all()
    #OVERWRITE or new experiment?
    #djangoPK = None
    global current_exp_id
    if len(existing_experiments) > 0:
        for current_exp in existing_experiments:
            # ascii_name = re.sub("[u']","",current_exp.name) #legacy regular expression!
            #Crazy Bug, 'u' was substituted. Dont see any need for reg subst anymore
            ascii_name = current_exp.name
            if ascii_name == name:
                print name , ' already exists!'
                print 'ID and Fixture will override an existing Experiment! (No changes to database.)'

                current_exp_id = current_exp.pk
                break
            else:
                # print ascii_name, name
                # print '### NO NAME MATCH ###'
                current_exp_id = SetExperimentDjangoPK() #django get unused experiment ID, counts existing exeriments + 1
    else:
        print '# Completely new database... initiating first project. #'
        current_exp_id = 1
    #djangoLANGUAGE = 'de' #has to be dynamic, will be gotten by admin form or by manual overwrite in the internal django admin app
    experiment_fields = r'"name":"%s","language":"%s"'
    experiment = ('eyevacs.Experiment', current_exp_id, experiment_fields % (name, language))
    global exp_filename
    exp_filename = 'EXP_' + name + '_' +language + '_' + str(current_exp_id) + '_FIX.json'
    full_path = fixture_output + exp_filename
    f = open (full_path, 'w')
    experiment_output = output % single_model % experiment
    f.write(experiment_output)
    f.close()

def LoadExpFixture(exp_json_filename):
#    relative_path =
    try:
        print '*** Importing external fixtures ***:'
        #print sys.executable, root,'\\manage.py loaddata', exp_json_filename
        #execfile('./manage.py loaddata ' + exp_json_filename)
        call([sys.executable, 'manage.py', 'loaddata', exp_json_filename])
        print '-- Imported ' + exp_json_filename +' sucessfully --'
    except:
        print '############### ERROR importing experiment...'
        print exp_json_filename

def InitPaths():
    #global vars
    global root
    global external_data_path
    global fixture_output
    global output_data_path

    #root path
    temp_root = sys.path[0]
    #regular expression substitution
    root = re.sub(r"\\","/",temp_root)
    external_data_path = './external_data/'
    fixture_output = './eyevacs/fixtures/' + experiment_name + '/'
    #Experiment fixture folder
    if not os.path.isdir(fixture_output):
        os.makedirs(fixture_output)
    #rnd data folder
    rnd_data_fullpath = './eyevacs/data/' + experiment_name + '/'
    if not os.path.isdir(rnd_data_fullpath):
        os.makedirs(rnd_data_fullpath)
    global output_data_path
    output_data_path = rnd_data_fullpath

def CreateDefaultRndScales():
    for i in range(0,len(default_scales),1):
        print default_scales[i]
        create_rnd_scale.main(current_exp_id, default_scales[i])

def CheckLang():
        lang_choices = ("de","en")
        choice = raw_input('Enter Language: "de" or "en": \n -->')
        if choice not in lang_choices:
            CheckLang()
        else:
            return choice

def CreateGrouping(exp, seed):
    try:
        exp.grouping.delete()
    except:
        print 'The experiment wasnt assigned a grouping yet.'
    grouping.main(exp, seed)


def Echo():
    if not switch_deadlock:
        print ''
        print 'Database Content:'
        print '-----------------'
        print '1. Experiment Count: ', Experiment.objects.count()
        print '1.1. Grouping Count: ', Grouping.objects.count()
        print '1.2. Attributes: ', Attribute.objects.count()
        print '1.2.1 Levels: ', Level.objects.count()
        print '2. Ext Src Data Count: ', External_Source_Data.objects.count()
        print '2.1. Ext Src Data SCALE Count: ', External_Source_Data.objects.filter(filetype = 'scale').count()
        print '3. Ext ChoiceTask Count: ', External_Choice_Task.objects.count()
        print '4. Ext BaselineCT Count: ', External_Baseline_Choice_Task.objects.count()
        print '5. Random Order Count: ', External_Order_Scale.objects.count()
        # print '6. Scales Count:' , Scale.objects.count()
        # print '7. Scale Questions Count: ', Scale_Question.objects.count()
        print ''

def FlushAll():
    Echo()
    sure = raw_input('FLUSHING ALL DJANGO MODEL OBJECTS!!!\n --- Are you sure? --- \n type "yes" to to DELETE!\n --- every other key to abort. ---')
    if sure == 'yes':
        Experiment.objects.all().delete()
        Attribute.objects.all().delete()
        Level.objects.all().delete()
        External_Source_Data.objects.all().delete()
        External_Choice_Task.objects.all().delete()
        External_Baseline_Choice_Task.objects.all().delete()
        External_Order_Scale.objects.all().delete()
        print '\n ### Objects have been deleted ###!\n'
    else:
        print '\n ### Deletion ABORTED ###! \n'
    Echo()

def Flush():
    Echo()
    Elements = [Experiment.objects.all(), Attribute.objects.all(), Level.objects.all(), External_Source_Data.objects.all(), External_Source_Data.objects.filter(filetype = 'scale'), External_Choice_Task.objects.all(), External_Baseline_Choice_Task.objects.all(), External_Order_Scale.objects.all()]
    for ind, ele in enumerate(Elements):
        print ind, ' -- ', ele,' \n'
    print '\n\n What do uo want to FLUSH?'
    print 'Enter all numbers seperated by ","!'
    to_flush = raw_input('-->')
    print to_flush.split(',')
    for element in to_flush.split(','):
        print Elements[int(element)], ' will be deleted. \n'
        sure = raw_input(' --- Are you sure? --- \n type "yes" to to DELETE!\n --- every other key to abort. ---\n -->')
        if sure == 'yes':
            Elements[int(element)].delete()
        else:
            print '\n ### Deletion ABORTED ###! \n'
    Echo()

def EchoDeadlock(single_exp_pk = None):
    if single_exp_pk == None:
        print ''
        print 'Deadlock related Database Content:'
        print '----------------------------------'
        print 'Experiment Count: ', Experiment.objects.count()
        exps = Experiment.objects.all()
        print '----------------------------------'
    else:
        exps = []
        single_exp = Experiment.objects.get(pk=single_exp_pk)
        exps.append(single_exp)
    for i,e in enumerate(exps):
        echostring = str(e.pk)+ '. '+ e.name +': '
        ct_files = e.external_source_data_set.filter(filetype = 'ctask')
        cts_used = 0
        cts_free = 0
        for f in ct_files:
            cts_used += f.external_choice_task_set.filter(used=True).count()
            cts_free += f.external_choice_task_set.filter(used=False).count()
        echostring += " ct files:"+str(len(ct_files))
        echostring += " used cts:"+str(cts_used)
        echostring += " free cts:"+str(cts_free)
        bsl_files = e.external_source_data_set.filter(filetype = 'bltsk')
        bsl_used = 0
        bsl_free = 0
        for f in bsl_files:
            bsl_used += f.external_baseline_choice_task_set.filter(used=True).count()
            bsl_free += f.external_baseline_choice_task_set.filter(used=False).count()
        echostring += " bsl files:"+str(len(bsl_files))
        echostring += " used bsl:"+str(bsl_used)
        echostring += " free bsl:"+str(bsl_free)

        print echostring
        for ct in ct_files:
            amount = ct.external_choice_task_set.all()[0].amount
            rangestring = str(i)+ '.       ct  amount: '+str(amount)
            rangestring += ' range start: '+ str(ct.range_start)
            rangestring += ' end: '+ str(ct.range_end)
            print rangestring
        for bsl in bsl_files:
            amount = bsl.external_baseline_choice_task_set.all()[0].amount
            rangestring = str(i)+ '.       bsl amount: '+str(amount)
            rangestring += ' range start: '+ str(bsl.range_start)
            rangestring += ' end: '+ str(bsl.range_end)
            print rangestring

def resetUsedExtData():
    print "Are you sure u want to RESET ALL 'USED' Data?"
    input_yes = raw_input("(y/n)")
    if input_yes == 'y':
        pcpts = Participant.objects.count()
        if pcpts == 0:
            cts_used = External_Choice_Task.objects.filter(used=True)
            bsl_used = External_Baseline_Choice_Task.objects.filter(used=True)
            rnd_used = External_Order_Scale.objects.filter(used=True)
            pubs     = Pub.objects.all()
            groupings = Grouping.objects.all()
            objects = [cts_used, bsl_used, rnd_used]
            # objects = [pub_cts, pub_scales, pub_bsls]
            with transaction.commit_on_success():
                for e in objects: #each object
                    for o in e: #each linked item of each object
                        o.used = False
                        o.linked_pub = None
                        o.save()
                for g in groupings:
                    g.counter = 0
                    g.id_holes = None
                    g.save()
                for p in pubs:
                    p.delete()
            return 1
        else:
            print 'ABORTING RESET - YOU ARE TRYING TO DELETE PARTICIPANT DATA!'
            return 0
    else:
        print 'ABORINTG RESET'
        return 0



def deadlock():
    '''Sets all cts/bslcts less than range_start AND above range_end to "used".

    Sets all ranges per file, per exp, manually. Echoes status of all exps and throws an error on wrong ranges. Input: starting point, approx pcpts. Outputs suggested sharing range end points per file.'''
    EchoDeadlock()
    print "\nExecuting DEADLOCK on existing existing experiments.\n"
    #ALL entries should be reset before usage
    if resetUsedExtData():
        print "reset ok"
        resetted = True
    if resetted:
        #actual deadlock
        #iterates over all exps
        exps = Experiment.objects.all()
        for e in exps:
            EchoDeadlock()
            print 'How many participants will be approximately in'
            print 'Exp '+ str(e.pk) +' ' + e.name +'?'
            try:
                raw_approx_pcpt_amount = int(input('Enter a positive integer:'))
                e.info += 'Approximate participants: '+str(raw_approx_pcpt_amount)
                e.save()
            except ValueError:
                print 'ABORTING - INVALID INTEGER'
            #modulo difference to divisor, results group with all the same size
            rest = raw_approx_pcpt_amount % 4
            if rest != 0:
                round_up_by = 4 - (raw_approx_pcpt_amount % 4)
            else:
                round_up_by = 0
            approx_pcpt_amount_per_group = (raw_approx_pcpt_amount + round_up_by) / 4
            #define range
            ct_files = e.external_source_data_set.filter(filetype = 'ctask')
            bsl_files = e.external_source_data_set.filter(filetype = 'bltsk')
            for ct in ct_files:
                amount = ct.external_choice_task_set.all()[0].amount
                rangestring = str(e.pk)+ '.       ct  '+str(amount)
                rangestring += '  range start:'+ str(ct.range_start)
                rangestring += '  end:'+ str(ct.range_end)
                print rangestring
                #output suggested starting point
                try:
                    highest_taked_id_hard = External_Choice_Task.objects.filter(amount=amount, used=True).order_by('-id_hard')[0].id_hard
                except IndexError:
                    highest_taked_id_hard = 0
                # print 'Highest taked id hard: ' + str(highest_taked_id_hard)
                try:
                    new_lower_range = int(input("Input new lower range:"))
                    #2x groups per file for regular cts
                    new_upper_range = new_lower_range + 2*approx_pcpt_amount_per_group
                    ct.range_start = new_lower_range
                    ct.range_end = new_upper_range
                    ct.save()
                except:
                    print '*Using previous value*'
                    new_lower_range = ct.range_start
                    new_upper_range = ct.range_end
                ctfile_cts = ct.external_choice_task_set.all().order_by('-pk')
                #char field on id hard was stupid. have to rely on id_hard being sorted according to the pk
                highest_id_hard = int(ctfile_cts[0].id_hard) +1
                deadblock_range = range(0,ct.range_start,1) + range(ct.range_end, highest_id_hard,1)
                # raise Exception(len(ctfile_cts),ct.id_hard,deadblock_range)
                with transaction.commit_on_success():
                    for ct in ctfile_cts:
                        if int(ct.id_hard) in deadblock_range:
                            #DEADBLOCKING
                            ct.used = True
                            # raise Exception(str(model_to_dict(ct)),len(ctfile_cts),ct.id_hard,deadblock_range)
                            #JUST USED, NO LINKS
                        else:
                            ct.used = False
                        ct.save()

            for bsl in bsl_files:
                amount = bsl.external_baseline_choice_task_set.all()[0].amount
                rangestring = str(e.pk)+ '.       bsl '+str(amount)
                rangestring += '  range start:'+ str(bsl.range_start)
                rangestring += '  end:'+ str(bsl.range_end)
                print rangestring
                #output suggested starting point
                try:
                    highest_taked_id_hard = External_Baseline_Choice_Task.objects.filter(amount=amount, used=True).order_by('-id_hard')[0].id_hard
                except IndexError:
                    highest_taked_id_hard = 0
                # print 'Highest taked id hard: ' + str(highest_taked_id_hard)
                try:
                    new_lower_range = int(input("Input new lower range:"))
                    new_upper_range = new_lower_range + approx_pcpt_amount_per_group
                    bsl.range_start = new_lower_range
                    bsl.range_end = new_upper_range
                    bsl.save()
                except:
                    print '*Using previous value*'
                    new_lower_range = bsl.range_start
                    new_upper_range = bsl.range_end
                bslfile_bsls = bsl.external_baseline_choice_task_set.all().order_by('-pk')
                highest_id_hard = int(bslfile_bsls[0].id_hard) +1
                deadblock_range = range(0,bsl.range_start,1) + range(bsl.range_end, highest_id_hard,1)
                with transaction.commit_on_success():
                    for bsl in bslfile_bsls:
                        # raise Exception(highest_id_hard, len(bslfile_bsls), deadblock_range)
                        if int(bsl.id_hard) in deadblock_range:
                            #DEADBLOCKING
                            bsl.used = True
                            #JUST USED, NO LINKS
                        else:
                            bsl.used = False
                        bsl.save()
    EchoDeadlock()

def main():

    print ''
    print '************************'
    print '* EyeVacs Start Script *'
    print '************************'
    print ''
    #Experiment
    #Create Fixture, input: name and language
    global experiment_name
    global fixture_output
    global switch_deadlock
    #DEBUG switches, do the work in CHUNCKS:
    #tested combinations:
    #1. chunk: <new_exp>, <ct>, <load_fixtures>
    #2. chunk: <default_rnd>, <load_fixtures>, <load_experimentsetup>
    switch_new_exp=                 0
    switch_ct =                     0 # use together with switch_load_fixtures
    #DONT USE _ct and default_rnd TOGETHER !!! ID PROBLEM
    switch_default_rnd =            0 # use together with switch_load_fixtures
    # switch_rnd = 0 #overridden by default rnd
    switch_load_fixtures =          0
    switch_load_experimentsetup =   0
    #3. chunk: <deadlock>
    #use if AFTER all experiments are created
    switch_deadlock =               1

    Echo()

    if not switch_deadlock:
        exps = Experiment.objects.all()
        print 'EXISTING EXPERIMENTS:'
        print '---------------------'
        for i,e in enumerate(exps):
            print str(i)+ '. '+ e.name
        if switch_new_exp:
            #NEW EXPERIMENT

            experiment_name = raw_input('\nEnter Name of EXPERIMENT: \n #####:')
            experiment_language = CheckLang()
            ext_seed =raw_input('\nEnter a SEED, <OR> leave blank : \n #####:')
        else:
            exps = Experiment.objects.all()
            last_exp = Experiment.objects.get(pk=len(exps))
            switch_to = raw_input('\nEnter the # of EXPERIMENT to work on, <OR> leave blank, to use <'+last_exp.name +'> : \n #####:')
            if not switch_to == "":
                #select experiement
                # try:
                if int(switch_to) < len(exps):
                    selected_pk = int(switch_to)+1
                    curr_exp = Experiment.objects.get(pk=selected_pk)
                else:
                    raise Exception('Invalid Project')
                # except:
                    # print 'except'
                    # raise Exception('Invalid Project')
            else:
                #LAST IMPORTED EXPERIMENT
                curr_exp = Experiment.objects.get(pk=len(exps))
            experiment_name = curr_exp.name
            experiment_language = curr_exp.language

        InitPaths()
        MakeExperiment(experiment_name, experiment_language)
        LoadExpFixture(fixture_output+ exp_filename)
        if switch_new_exp:
            #includes a default seed
            if not ext_seed == '':
                try:
                    seed = int(ext_seed)
                    CreateGrouping(Experiment.objects.get(pk=current_exp_id), seed)
                except:
                    raise Exception('Couldn\'t typecast the seed to int.')
            else:
                CreateGrouping(Experiment.objects.get(pk=current_exp_id), None)
        print ' ### CURRENT EXP ID:', current_exp_id
        if switch_ct:
            create_fixtures.main(current_exp_id, external_data_path, fixture_output)
        #kind of obsolete
        # if switch_rnd:
            # create_rnd_scale.main(current_exp_id)
        if switch_default_rnd:
            CreateDefaultRndScales()
        if switch_load_fixtures:
            print root
            load_fixtures.Run(root, fixture_output[1:], output_data_path[1:])
        # if switch_load_scale_questions:
        #     curr_exp = Experiment.objects.get(pk = current_exp_id )
        #     scale_questions.load_scale_questions(curr_exp)
        if switch_load_experimentsetup:
            # try:
            curr_exp.attribute_set.all().delete()
            # curr_exp.level_set.all().delete()
            print ' --- flushed old Attributes & Levels ---'
            # except:
                # print ' --- "'+curr_exp.name+'" must be new, installing current Attributes & Levels... ---'
            # Attribute.objects.all().delete()
            # Level.objects.all().delete()
            load_setup.main(curr_exp)
        Echo()

    elif switch_deadlock:
        deadlock()

    print '___________________________'
    # print 'Everthing went as expected!'


main()

#if __name__ == "__main__":
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djVacs.settings")
    #from django.core.management import execute_from_command_line
    #execute_from_command_line(sys.argv)
    #__main__()

#execfile('./start.py')
