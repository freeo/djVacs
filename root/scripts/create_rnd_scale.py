import random
from eyevacs.models import Experiment, External_Source_Data, External_Order_Scale

data_path = ''
filename = 'SEEDS_%s.csv'
init_list = []
default_amount = 900
experiment_name = ''
experiment_id = None

def init_list(lower, upper):
    output = []
    for i in range(lower, upper+1, 1):
        output.append(i)
    init_list = output

def register_seed(seed):
    used_seeds = open(data_path + filename, 'w')
    used_seeds.write(seed)
    used_seeds.close()



def create_seed():
    seed = random.int(100000,999999)
    seeds = []
    used_seeds = open(data_path + filename, 'w')
    for i in range(0,len(used_seeds),1):
        seeds.append(used_seeds.readline())
        if seeds[i] == seed:
            create_seed()
            break
    used_seeds.close()
    return seed

def shuffle_scale(lower, upper):
    seed = create_seed()
    rnd = random.Random(seed)
    tidy = init_list(lower, upper)
    def return_shuffle(array):
        rnd.shuffle(array)
        return array
    orderings = []
    #header
    ordering.append(filename[:-3] + str(default_amount) + str(seed))
    for i in range(0, default_amount,1):
        ordering.append(return_shuffle(tidy))
    return orderings

def GetExtSrcDataDjangoPK():
    return External_Source_Data.objects.count() + 1

def write_json():
    #writes a list to json
    #subs: pk, fields
    ext_source_data = '{"model":"eyevacs.External_Source_Data","pk":"%s","fields":"%s"}'
    #subs: header expname expid
    ext_source_data_fields = '{"filetye":"scale","header":"%s","exp_name":"%s","experiment":"%s"}'
    output = '[%s, %s]'
    pk = GetExtSrcDataDjangoPK()


def main(ext_data_path, exp_id):
    global data_path
    global experiment_name
    global experiment_id
    global filename
    exp = Experiment.objects.get(pk=exp_id)
    experiment_name = exp.name
    current_exp_id = exp.pk
    data_path = ext_data_path
    experiment_id = exp_id
    name = raw_input('Enter Name of Order (Scales name):\n')
    print name
    filename = filename % name
    lower = raw_input('Lower limit:\n')
    upper = raw_input('Upper limit:\n')

    untidy = shuffle_scale(lower, upper) #includes header with its seed
    write_json(untidy)

if __name__ == '__main__':
    import sys
    args = sys.argv
    main(args[1],args[2])
'''
execfile('./scripts/create_rnd_scale.py')
main('E:\djVacs\root./external_data/', 1)
'''
