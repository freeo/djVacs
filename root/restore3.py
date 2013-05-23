from eyevacs.models import Participant, Pub, Experiment
from django.forms.models import model_to_dict

mel = Experiment.objects.get(pk=3)
pcpts = mel.participant_set.all()

corrupt_cts = [9001,9901,7201,8101]
columns = ['ct1pk', 'ct2pk', 'ct3pk', 'ct4pk', 'ct5pk', 'ct6pk', 'ct7pk', 'ct8pk']
corr_pcpts = []
for p in pcpts:
    for c in columns:
        # print getattr(p, c)
        if int(getattr(p, c)) in corrupt_cts:
            if not p.id in corr_pcpts:
                corr_pcpts.append(p.id)

print len(corr_pcpts)
print corr_pcpts
print [ Participant.objects.get(id=p).hard_id for p in corr_pcpts]
print [ Participant.objects.get(id=p).def_group for p in corr_pcpts]
