'''
Program Name: Initial Data Loading Script for EYEVACS

Author: Arthur Jaron
Decsription: Loads initial external data files, creates JSON fixtures of them and loads them into th sqlite database of an existing or new EXPERIMENT Object of the EYEVACS Django application
'''

import sys
import os
from eyevacs.models import Experiment, External_Source_Data, External_Choice_Task, External_Order_Scale

'''
global variables
'''

experiment_name = ''
extsrcdata_fixture_counter = External_Source_Data.objects.count()

print '\n!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
print '\n'
print 'LOADING INITIAL DATA SCRIPT'
print '\n'
print '\n!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'


#testing proper relative addressing by printing an echo from the correct folder:
execfile("./initial_data/init_data_echo.py")
#Note: "../" gives the parent folder


#Steps:
init_path = "./initial_data/"
dirlist = os.listdir(init_path)
print 'Files of ', init_path,': '
print dirlist
#filename = raw_input('enter filename to convert to xml fixture: \n')
#csv_file = open(init_path + filename, 'r')

#list header of first opened file
#for i in range(0,5,1):
#    print csv_file.readline()

csv_lists = []
for i in range(0,len(dirlist),1):
    if '.csv' in dirlist[i]:
        csv_file = open(init_path + dirlist[i], 'r')
        csv_list = csv_file.readlines()
        csv_lists.append(csv_list)

'''
#checking header of all imported files
for i in range(0,len(csv_lists),1):
    print csv_lists[i][0]
    print csv_lists[i][1]
    print csv_lists[i][2]
    print csv_lists[i][3]
    print csv_lists[i][4]
'''
def ConvStringlist(thestring):
    return thestring.split(',',thestring.count(','))

def Analyze_List(current):
    total_tasks = ConvStringlist(current[len(current)-1])[0]
#    print 'total tasks: '+ total_tasks
    counter = 1
    for i in range(2,9,1):
        if ConvStringlist(current[i])[0] == ConvStringlist(current[i-1])[0]:
            counter += 1
        else:
            break
#    print 'counter: '+str(counter)
    return (counter, total_tasks)

def GetExperimentDjangoPK():
    '''Gets a free personal key identifier for a new Experiment Model.'''

    exp_count = Experiment.objects.count()
    print 'Existing Experiments: ', exp_count
    return exp_count + 1

def GetExtSrcDataDjangoPK():
    '''Gets a free personal key identifier for a new EXTERNAL SOURCE DATA Model.'''

    exp_count = External_Source_Data.objects.count()
    global extsrcdata_fixture_counter
    if extsrcdata_fixture_counter >= exp_count:
        extsrcdata_fixture_counter += 1
    return extsrcdata_fixture_counter


    print 'Existing EXT SRC DATA: ', exp_count
    return exp_count + 1


def MakeFixture(model, amount, total_tasks):
    '''creates the string frame of the JSON format for a generic model.

    will be used for 3 types of models: external_choice_task, external_source_data, external_order_scale. Basically an easy string with an "%s" in the middle, which contains the actual model data, which has to be provided via the argument "model".

output in models:
1 external_source_data fixture
x external_choice_task fixtures (x = total_tasks divided by amount).'''
    #local strings
    single_model = r'{"model":"%s","pk":%s,"fields":{%s}}'
    output = "[%s,\n%s]"

    #EXTERNAL_SOURCE_DATA ctask Object
    ext_data_pk = GetExtSrcDataDjangoPK()
    ext_data_fields = r'"filetype":"ctask","header":"%s","experiment":"%s"' % (model[0].rstrip('\n'), experiment_name)
    ext_data_model = single_model % ("eyevacs.External_Source_Data", ext_data_pk, ext_data_fields)
    #Testing the output:
    #print 'External data Fixture: \n'
    #print ext_data_model

    #EXTERNAL_CHOICE_TASK 's !!!! DIRECT OUTPUT TO EXTERNAL FILE, because of huge output!
    fixturename = experiment_name + '_CT' +str(amount)+'_ID'+str(ext_data_pk)+'.JSON'
    print fixturename, '\n'

    tempfile = open (init_path + fixturename, 'w')

    ctask_list = []*total_tasks
    ext_ct_fields = r'"id_hard":"%s","source_file":"%s","amount":"'+str(amount)+r'"used":"False","linked_pcpt":"%s"'
    ext_ct_model =
    for i in range(1, total_tasks+1,1):
        for j in range (1,amount+1,1):
            single_model % 
            ctask_list[i]model[i*j]




def MakeExperiment(name, language):
    '''Create an Experiment Model Fixture.'''
    single_model = r'{"model":"%s","pk":%s,"fields":{%s}}'
    output = "[%s]"
    djangoPK = GetExperimentDjangoPK() #django get unused experiment ID, counts existing exeriments + 1
    #djangoLANGUAGE = 'de' #has to be dynamic, will be gotten by admin form or by manual overwrite in the internal django admin app
    experiment_fields = r'"name":"%s","language":"%s"'
    experiment = ('eyevacs.Experiment', djangoPK, experiment_fields % (name, language))
    print output % single_model % experiment



def main():
    '''Processing all found .csv files in folder ./initial_data/'''

    #Experiment
    #Create Fixture, input: name and language
    global experiment_name
    #TEMP experiment_name = raw_input('Enter Name of EXPERIMENT to CREATE/OVERWRITE: \n -->')
    experiment_name = 'OXIQUATL'
    lang_choices = ("de","en")
    def CheckLang():
        choice = raw_input('Enter Language, possible choices: "de" or "en": \n -->')
        if choice not in lang_choices:
            CheckLang()
        else:
            return choice
    experiment_language = CheckLang()
    MakeExperiment(experiment_name, experiment_language)

    #External Data AND Choice Task
    data_properties = []
    fixtures_list = [] #one fixture object contains both, the header object DATA and all appendant choice tasks
    for i in range(0,len(csv_lists),1):
        data_properties.append(Analyze_List(csv_lists[i]))
        fixtures_list.append(MakeFixture(csv_lists[i], data_properties[i][0],data_properties[i][1]))

    ##checking temp results
    print data_properties

main()



#.load csv to model object


#db_ct_id_2.csv

#register file name to db (needs new model!), check for existency

#.model object to xml (fixture data)

#.import fixture data

#.done: sql can use the choice task columns, mapped by the yet undefined "model object"

I9100XXLQ6
