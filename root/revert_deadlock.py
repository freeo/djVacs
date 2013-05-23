from eyevacs.models import Participant, Pub, Experiment, External_Source_Data, External_Choice_Task
from django.forms.models import model_to_dict
from django.db import transaction


'''initiate needed database objects '''

mel = Experiment.objects.get(pk=3)
pcpts = mel.participant_set.all()
taskfiles = mel.external_source_data_set.filter(filetype="ctask")
print "amount of taskfiles: ", len(taskfiles)

echo = 0
revert_deadlock = 0 #only partially, the specific range from 'echo', the value of 100 is arbitrary
show_connections = 1


'''determine relevant data ranges'''
if echo:
    for i in range(len(taskfiles)):
        tasks = taskfiles[i].external_choice_task_set.all()
        counter = 0
        max_hard_id = 0
        min_hard_id = 5000000
        for t in tasks:
            if t.linked_pcpt != None:
                counter += 1
                if int(t.id_hard) > max_hard_id:
                    max_hard_id = int(t.id_hard)
                if int(t.id_hard) < min_hard_id:
                    min_hard_id = int(t.id_hard)

        print "taskfile ", t.amount, ": ", counter, " max: ", max_hard_id, " min: ", min_hard_id

'''apply "unused" state from id_hard 200 - 299 per file'''
'''testing first: GET the cts to manipulate!
they are: unlinked, strictly above 199 id_hard'''
if revert_deadlock:
    for i in range(len(taskfiles)):
        tasks = taskfiles[i].external_choice_task_set.all()
        freeup_range = range(200,300,1) #WITHOUT 300!
        new_unused_cts = []
        error_linkeds = []
        unuseds = [] #HAS to be empty! deadlock 'used' them in first place, purpose of this is to revert the false 'used' status
        all_used = True
        for t in tasks:
            if int(t.id_hard) in freeup_range:
                new_unused_cts.append(t)
                # new_unused_cts.append(t.used) #.id_hard only for testing
                if t.linked_pcpt != None:
                    error_linkeds.append(t)
                if not t.used:
                    unuseds.append(t.id_hard)
                if not t.used:
                    all_used = False

        print "taskfile ", t.amount, ": ", len(new_unused_cts)
        # print new_unused_cts, ''
        print "errors: ", error_linkeds
        # print "not in use: ", unuseds
        print "all used? ", all_used
        print ''

        if all_used: #last check
        # if 1: #last check
            with transaction.commit_on_success():
                for t in new_unused_cts:
                    t.used = False
                    t.save()

            print "reverted ", [t.id_hard for t in new_unused_cts], " to USED=FALSE!"

if show_connections:
    for i in range(len(taskfiles)):
        tasks = taskfiles[i].external_choice_task_set.all()
        max_hard_id = 0
        for t in tasks:
            if t.linked_pcpt != None:
                if int(t.id_hard) > max_hard_id:
                    max_hard_id = int(t.id_hard)
        last_task = tasks.get(id_hard=int(max_hard_id))

        print last_task.id_hard, last_task.id







'''testing if range is a correct LIST'''
# freeup_range = range(200,300,1) #WITHOUT 300!
# print freeup_range


