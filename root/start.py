import os
import sys
import re
from scripts import load_fixtures, create_fixtures, create_rnd_scale
from subprocess import call
from eyevacs.models import Experiment, External_Source_Data, External_Choice_Task, External_Order_Scale, External_Baseline_Choice_Task

#paths
root = sys.path[0]
external_data_path = './external_data/'
fixture_output = './eyevacs/fixtures/'
output_data_path = './eyevacs/'
experiment_name = ''
exp_filename = ''
current_exp_id = None

def SetExperimentDjangoPK():
    '''Gets a free personal key identifier for the new current Experiment Model.'''

    global current_exp_id
    exp_count = Experiment.objects.count()
    # print 'Existing Experiments: ', exp_count
    current_exp_id = exp_count + 1
    return current_exp_id

def MakeExperiment(name, language):
    '''Create an Experiment Model Fixture.'''

    single_model = r'{"model":"%s","pk":%s,"fields":{%s}}'
    output = "[%s]"
    existing_experiments = Experiment.objects.all()
    #OVERWRITE or new experiment?
    djangoPK = 1
    for current_exp in existing_experiments:
        ascii_name = re.sub("[u']","",current_exp.name) #regular expression!
        if ascii_name == name:
            print name , ' already exists!'
            print 'ID and Fixture will override an existing Experiment! (No changes to database.)'
            global current_exp_id
            djangoPK = current_exp_id = current_exp.pk
            break
        else:
            djangoPK = SetExperimentDjangoPK() #django get unused experiment ID, counts existing exeriments + 1
    #djangoLANGUAGE = 'de' #has to be dynamic, will be gotten by admin form or by manual overwrite in the internal django admin app
    experiment_fields = r'"name":"%s","language":"%s"'
    experiment = ('eyevacs.Experiment', djangoPK, experiment_fields % (name, language))
    global exp_filename
    exp_filename = 'EXP_' + name + '_' +language + '_' + str(djangoPK) + '_FIX.json'
    full_path = fixture_output + experiment_name + '/' + exp_filename
    f = open (full_path, 'w')
    experiment_output = output % single_model % experiment
    f.write(experiment_output)
    f.close()

def LoadExpFixture(exp_json_filename):
#    relative_path = 
    try:
        print '\n*** Importing external fixtures ***: \n'
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
    print root

    external_data_path = './external_data/'
    fixture_output = './eyevacs/fixtures/'
    #Experiment fixture folder
    if not os.path.isdir(fixture_output):
        os.makedirs(fixture_output)
    #rnd data folder
    rnd_data_fullpath = './eyevacs/data/' + experiment_name + '/'
    if not os.path.isdir(rnd_data_fullpath):
        os.makedirs(rnd_data_fullpath)
    global output_data_path
    output_data_path = rnd_data_fullpath



def main():
    print '********************'
    print '*Script starting...*'
    print '********************'
    print ''
    #Experiment
    #Create Fixture, input: name and language
    global experiment_name
    global fixture_output
    #DEBUG switches
    switch_exp_name_on = 0
    switch_rnd = 1
    if switch_exp_name_on:
        experiment_name = raw_input('Enter Name of EXPERIMENT: \n -->')
    else:
        experiment_name = 'OXIQUATL'
    lang_choices = ("de","en")
    def CheckLang():
        choice = raw_input('Enter Language: "de" or "en": \n -->')
        if choice not in lang_choices:
            CheckLang()
        else:
            return choice
    experiment_language = CheckLang()
    fixture_output += experiment_name + '/'

    InitPaths()

    MakeExperiment(experiment_name, experiment_language)
    if not switch_rnd:
        LoadExpFixture(fixture_output+ exp_filename)
        create_fixtures.main(current_exp_id, external_data_path, fixture_output)
        load_fixtures.Run(root, fixture_output)
        #create_rnd_scale.main(root + external_data_path, current_exp_id)
    else:
        #create_rnd_scale.main(root + output_data_path[1:], current_exp_id)
        create_rnd_scale.main(current_exp_id)

main()

if __name__ == "__main__":
    print ' hezho'
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djVacs.settings")
    #from django.core.management import execute_from_command_line
    #execute_from_command_line(sys.argv)
    __main__()

#execfile('./start.py')
