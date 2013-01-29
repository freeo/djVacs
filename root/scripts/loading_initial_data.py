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
extctdata_fixture_counter = External_Choice_Task.objects.count()

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
output_path ='./eyevacs/fixtures/'
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
    output = thestring.rstrip('\n')
    return output.split(',',thestring.count(','))

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
    '''Gets a free personal key identifier for the new current Experiment Model.'''

    global current_exp_id
    exp_count = Experiment.objects.count()
    # print 'Existing Experiments: ', exp_count
    current_exp_id = exp_count + 1
    return current_exp_id

def GetExtSrcDataDjangoPK():
    '''Gets a free personal key identifier for a new EXTERNAL SOURCE DATA Model.'''

    exp_count = External_Source_Data.objects.count()
    global extsrcdata_fixture_counter
    if extsrcdata_fixture_counter >= exp_count:
        extsrcdata_fixture_counter += 1
    return extsrcdata_fixture_counter

    print 'Existing EXT SRC DATA: ', exp_count
    return exp_count + 1

def GetExtCTDjangoPK():
    global extctdata_fixture_counter
    extctdata_fixture_counter += 1
    return extctdata_fixture_counter

def PrepareHeaderForFixture(rawHeader):
    t1 = rawHeader.rstrip('\n')
    out = t1.replace('"','')
    return out

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
    header = PrepareHeaderForFixture(model[0])
    ext_data_fields = r'"filetype":"ctask","header":"%s","exp_name":"%s","experiment":%s' % (header, experiment_name, GetExperimentDjangoPK())
    ext_data_model = single_model % ("eyevacs.External_Source_Data", ext_data_pk, ext_data_fields)
    #Testing the output:
    #print 'External data Fixture: \n'
    #print ext_data_model

    #EXTERNAL_CHOICE_TASK 's 
    #template strings
    ext_ct_model = r'{"model":"eyevacs.External_Choice_Task","pk":%s,"fields":{%s}}'
    ext_ct_fields = r'"id_hard":"%s","ext_src_data":"%s","ext_src_data_name":"%s","amount":%s,"used":false,"linked_pcpt":%s'
    ext_ct_ax = r',"raw_src_line":"%s","a1":"%s","a2":"%s","a3":"%s","a4":"%s","a5":"%s","a6":"%s","a7":"%s","a8":"%s"'

#collecting data from file and export string
    print 'total tasks: ', total_tasks
    ctask_list = []
    ext_src_data_name = "CT_" + str(amount) + "_" + total_tasks +"_"+experiment_name
    print 'model length', len(model)
    for i in range(0, int(total_tasks),1):
        #if i < 10:
        #    print "i+", i
        CT_DjangoPK = GetExtCTDjangoPK()
        a0 =  " | "
        concept_list = ["-"]*8
        ext_ct_fields_data = (str(i), ext_data_pk, ext_src_data_name, amount, "null")
        for j in range (0,amount,1):
            #if i*amount+j < 10:
            #    print "j#",j
            #    print "M",i*amount+j
            index = i*amount+j+1 #skipping header
            currentLine = ConvStringlist(model[index]) #is a list
            a0 += model[index].rstrip('\n') +  " | "
            concept_list[int(currentLine[2])-1] = currentLine[3:9]
        a1 = concept_list[0]
        a2 = concept_list[1]
        a3 = concept_list[2]
        a4 = concept_list[3]
        a5 = concept_list[4]
        a6 = concept_list[5]
        a7 = concept_list[6]
        a8 = concept_list[7]
        ext_ct_ax_data = (a0,a1,a2,a3,a4,a5,a6,a7,a8)

        ct_output = ext_ct_model % (CT_DjangoPK, (ext_ct_fields % ext_ct_fields_data) + (ext_ct_ax % ext_ct_ax_data))
        ctask_list.append(ct_output)
    #!!!! DIRECT OUTPUT TO EXTERNAL FILE
    fixturename = experiment_name + '_CT' +str(amount)+'_ID'+str(ext_data_pk)+'.json'
    print fixturename, '\n'
    tempfile = open (output_path + fixturename, 'w')
    tempfile.write("[" + ext_data_model + ",\n")
    for k in range(0,len(ctask_list)-1,1):        
        tempfile.write(str(ctask_list[k]) + ',\n')
    #LAST ENTRY MUST OMIT ',' BECAUSE OF .JSON File Format!
    tempfile.write(str(ctask_list[len(ctask_list)-1]) + '\n')
    tempfile.write("]")
    tempfile.close()

def MakeExperiment(name, language):
    '''Create an Experiment Model Fixture.'''
    single_model = r'{"model":"%s","pk":%s,"fields":{%s}}'
    output = "[%s]"
    djangoPK = GetExperimentDjangoPK() #django get unused experiment ID, counts existing exeriments + 1
    #djangoLANGUAGE = 'de' #has to be dynamic, will be gotten by admin form or by manual overwrite in the internal django admin app
    experiment_fields = r'"name":"%s","language":"%s"'
    experiment = ('eyevacs.Experiment', djangoPK, experiment_fields % (name, language))
    filename = 'EXP_' + name + '_' +language + '_' + str(djangoPK) + '_FIX.json'
    f = open (output_path + filename, 'w')
    experiment_output = output % single_model % experiment
    f.write(experiment_output)
    f.close()

def main():
    '''Processing all found .csv files in folder ./initial_data/'''

    #Experiment
    #Create Fixture, input: name and language
    global experiment_name
    experiment_name = raw_input('Enter Name of EXPERIMENT to CREATE/OVERWRITE: \n -->')
    #experiment_name = 'OXIQUATL'
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

