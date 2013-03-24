from eyevacs.models import Experiment,Grouping
import random
import json

exp = None
#mersenne twister
#was only valid for 3 group setup!
# default_seed = 3935842

default_seed = 3565370 #tested for bielefeld
monash_seed = 5194735 #up to 300 participants watched at!
#1. increasing 2. decreasing 3. baseline

def createGrouping(seed):
    rnd = random.Random()
    rnd.seed(seed)
    grouping = [0]*900
    for i in range(0,900,1):
        grouping[i] = rnd.randint(1,4)
    return grouping
    # proc_grouping = re.sub(',','\n',str(grouping))[1:-1]

    # fname = 'grp_%s.csv' % seed
    # f = open(fname, 'w')
    # f.write(str(seed) + '\n')
    # f.write(proc_grouping)
    # f.close()
    # print grouping

def main(curr_exp, ext_seed):
    global exp
    exp = curr_exp
    if ext_seed == None:
        use_seed = default_seed
    else:
        use_seed = ext_seed
    grouping = createGrouping(use_seed)
    print grouping[0:25]
    grouping_json = json.dumps(grouping)
    hard_grouping = Grouping(experiment = exp, seed = use_seed, counter = 0, group_nr = grouping_json)
    hard_grouping.save()
    print ' --- Grouping seed %s saved to experiment %s ---' % (str(use_seed) , exp.name)


# myModel = MyModel()
# listIWantToStore = [1,2,3,4,5,'hello']
# myModel.myList = json.dumps(listIWantToStore)
# myModel.save()


