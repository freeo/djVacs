from django.contrib.sessions.models import Session
from eyevacs.models import Participant, Pub
from django.forms.models import model_to_dict

sessions_coded = Session.objects.all()
sessions = [i.get_decoded() for i in sessions_coded]
sess130 = []
sess147 = []
print sessions[756]['pub']
inc = 0
for s in sessions:
    # print inc
    inc += 1
    try:
        # print s['pub']
        if s['pub']['hard_id'] == 130:
            sess130.append(s)
        if s['pub']['hard_id'] == 147:
            sess147.append(s)
    except (KeyError, TypeError):
        print 'key "pub" or key "hard_id" does not exist, life goes on...'
    except:
        # print 'key "pub" or key "hard_id" does not exist, life goes on...'
        pass

print '130 :',len(sess130), ', 147: ',len(sess147)
# print (sess130)
s130_1 = sess130[0]
print s130_1['pub']['def_group']
for ct_id in s130_1['pub_ctlist']:
    print ct_id.id
    # print model_to_dict(ct_id)

print "\nNEXT PCPT SESSION...\n"

s130_2 = sess130[1]
print s130_2['pub']['def_group']
for ct_id in s130_2['pub_ctlist']:
    print ct_id.id
    # print model_to_dict(ct_id)

print "\nNEXT PCPT SESSION...\n"

s147_1 = sess147[0]
print s147_1['pub']['def_group']
for ct_id in s147_1['pub_ctlist']:
    print ct_id.id

print "\nNEXT PCPT SESSION...\n"

s147_2 = sess147[1]
print s147_2['pub']['def_group']
for ct_id in s147_2['pub_ctlist']:
    print ct_id.id

