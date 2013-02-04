'''
Program Name: Initial Data Loading Script for EYEVACS

Author: Arthur Jaron
Decsription: Loads initial external data files, creates JSON fixtures of them. Creates Fixture of a new EXPERIMENT Object of the EYEVACS Django application.
'''

import sys
import os
from eyevacs.models import Experiment, External_Source_Data, External_Choice_Task, External_Order_Scale, External_Baseline_Choice_Task

'''
global variables
'''

experiment_name = ''
extsrcdata_fixture_counter = None
extctdata_fixture_counter = None
extbsldata_fixture_counter = None
current_exp_id = None

#testing proper relative addressing by printing an echo from the correct folder:
#execfile("./initial_data/init_data_echo.py")
#Note: "../" gives the parent folder


#Steps:
init_path = ""
output_path =''

def initDjangoPKcounters():
    global extsrcdata_fixture_counter
    global extctdata_fixture_counter
    global extbsldata_fixture_counter
    extsrcdata_fixture_counter = External_Source_Data.objects.count()
    extctdata_fixture_counter = External_Choice_Task.objects.count()
    extbsldata_fixture_counter = External_Baseline_Choice_Task.objects.count()

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

def GetExtBSLDjangoPK():
    global extbsldata_fixture_counter
    extbsldata_fixture_counter += 1
    return extbsldata_fixture_counter

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
    print '-- EXP ID: ',GetExperimentDjangoPK() , ' --'
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
    ctask_list = []
    ext_src_data_name = "CT_" + str(amount) + "_" + total_tasks +"_"+experiment_name
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

    tempfile = open (output_path + fixturename, 'w')
    tempfile.write("[" + ext_data_model + ",\n")
    for k in range(0,len(ctask_list)-1,1):
        tempfile.write(str(ctask_list[k]) + ',\n')
    #LAST ENTRY MUST OMIT ',' BECAUSE OF .JSON File Format!
    tempfile.write(str(ctask_list[len(ctask_list)-1]) + '\n')
    tempfile.write("]")
    tempfile.close()
    print '-- ', fixturename, ' --'
    print 'total tasks: ', total_tasks
    print 'model length', len(model)
    print ''

def MakeBaselineFixture(model):
    '''Similar to MakeFixture, but for baseline choice task files.'''

    #Return maximum of current task. Ordering of the file helps minimizing iteration.
    total_tasks = ConvStringlist(model[len(model)-1])[0]
    bsl_max_cts = 0
    for j in range(1,len(model),1):
        current = ConvStringlist(model[j])
        current_tasks = int(current[1]) # header: 0 Version, 1 Task, Concept, ...
        if bsl_max_cts <= current_tasks:
            bsl_max_cts = current_tasks
        else:
            break
    #XXX
    print '-- Max Baseline CTs: ' + str(bsl_max_cts) + ' --'
    
    #basic strings
    single_model = r'{"model":"%s","pk":%s,"fields":{%s}}'
    #EXTERNAL_SOURCE_DATA ctask json fixture
    ext_data_pk = GetExtSrcDataDjangoPK()
    header = PrepareHeaderForFixture(model[0])
    ext_data_fields = r'"filetype":"ctask","header":"%s","exp_name":"%s","experiment":%s' % (header, experiment_name, GetExperimentDjangoPK())
    print '-- ID: ',GetExperimentDjangoPK() , ' --'
    ext_data_model = single_model % ("eyevacs.External_Source_Data", ext_data_pk, ext_data_fields)

    #EXTERNAL_BASELINE_CHOICE_TASK fixtures
    #template strings
    ext_ct_model = r'{"model":"eyevacs.External_Baseline_Choice_Task","pk":%s,"fields":{%s}}'
    ext_ct_fields = r'"id_hard":"%s","task":%s,"ext_src_data":"%s","ext_src_data_name":"%s","used":false,"linked_pcpt":%s'
    ext_ct_ax = r',"raw_src_line":"%s","a1":"%s","a2":"%s","a3":"%s","a4":"%s","a5":"%s"'

    ctask_list = []
    ext_src_data_name = "CT_BSL_" + str(bsl_max_cts) + "_" + total_tasks +"_"+experiment_name
    print '-- Baseline length:', len(model) , ' --'
    for i in range(0, int(total_tasks),1): #participant: ID_HARD
        for j in range (0,int(bsl_max_cts),1): #pcpt.task
            BSL_DjangoPK = GetExtBSLDjangoPK()
            a0 =  " | "
            concept_list = ["-"]*5
            for k in range(0,5,1): #pcpt.task.concept
                index = i*int(bsl_max_cts)*5+j*5+k+1 #skipping header                
                currentLine = ConvStringlist(model[index]) #is a list
                a0 += model[index].rstrip('\n') +  " | "
                concept_list[int(currentLine[2])-1] = currentLine[3:9]
            a1 = concept_list[0]
            a2 = concept_list[1]
            a3 = concept_list[2]
            a4 = concept_list[3]
            a5 = concept_list[4]
            #if i < 150:
            #    print i, index, BSL_DjangoPK
            ext_ct_fields_data = (str(i+1), j+1 ,ext_data_pk, ext_src_data_name, "null")
            ext_ct_ax_data = (a0,a1,a2,a3,a4,a5)

            ct_output = ext_ct_model % (BSL_DjangoPK, (ext_ct_fields % ext_ct_fields_data) + (ext_ct_ax % ext_ct_ax_data))
            ctask_list.append(ct_output)

    #OUTPUT TO EXTERNAL FILE
    fixturename = experiment_name + '_CT_BSL' +str(bsl_max_cts)+'_ID'+str(ext_data_pk)+'.json'
    #print fixturename
    tempfile = open (output_path + fixturename, 'w')
    #Parent Object
    tempfile.write("[" + ext_data_model + ",\n")
    #Child Object
    #print '-- Baseline length: ', len(ctask_list), ' --'
    for l in range(0,len(ctask_list)-1,1):
        tempfile.write(str(ctask_list[l]) + ',\n')
    #LAST ENTRY MUST OMIT ',' BECAUSE OF .JSON File Format!
    tempfile.write(str(ctask_list[len(ctask_list)-1]) + '\n')
    tempfile.write("]")
    tempfile.close()
    #print '\n-- Baseline fixture '+ fixturename + ' created --'
    print '-- ', fixturename, ' --'
    print 'total tasks: ', total_tasks
    print 'model length', len(model)
    print '\n'


def main(exp_id, ext_data_path, fixture_path):
    '''Processing all found .csv files in folder ./initial_data/'''

    print '\n***********************\n'
    print '    Creating Fixtures'
    print '\n***********************\n'

    #Baseline CT Group: Amount of alternatives
    bsl_amount = 5

    global experiment_name
    global current_exp_id
    global init_path
    global output_path
    print 'EXP IOD', exp_id
    exp = Experiment.objects.get(pk=exp_id)
    experiment_name = exp.name
    current_exp_id = exp.pk
    init_path = ext_data_path
    output_path = fixture_path

    initDjangoPKcounters()

    #load ext data files
    dirlist = os.listdir(init_path)
    print 'Files of', init_path,': '
    print dirlist
    csv_lists = []
    csv_filenames = []
    for i in range(0,len(dirlist),1):
        if '.csv' in dirlist[i]:
            csv_file = open(init_path + dirlist[i], 'r')
            csv_list = csv_file.readlines()
            csv_lists.append(csv_list)
            csv_filenames.append(dirlist[i])
    print '-- ',len(csv_lists),' CSVs found! --'

    #Parse files to fixtures
    #A fixture object contains: 
    #the header object of Ext Source DATA and all appendant Ext Source Choice Tasks 
    data_properties = []
    fixtures_list = [] 
    for i in range(0,len(csv_lists),1):
        if not 'baseline' in csv_filenames[i].lower():
            data_properties.append(Analyze_List(csv_lists[i]))
            fixture = MakeFixture(csv_lists[i], data_properties[i][0],data_properties[i][1])
            fixtures_list.append(fixture)
        else:
            data_properties.append(Analyze_List(csv_lists[i]))
            MakeBaselineFixture(csv_lists[i])

