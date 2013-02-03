import random
from eyevacs.models import Experiment, External_Source_Data, External_Order_Scale

data_path = ''
fixture_path = ''
seedname = ''
filename = ''
init_list = []
default_amount = 900
experiment_name = ''
experiment_id = None
order_counter = None

def init_list(lower, upper):
    output = []
    for i in range(lower, upper+1, 1):
        output.append(i)
    return output

def register_seed(seed):
    used_seeds = open(data_path + seedname, 'w')
    used_seeds.write(str(seed))
    used_seeds.close()

def create_seed():
    seed = random.randint(100000,999999)
    seeds = []
    used_seeds = open(data_path + seedname, 'w')
    try:
        for i in range(0,len(used_seeds),1):
            seeds.append(used_seeds.readline())
            if int(seeds[i]) == seed:
                create_seed()
                break
        used_seeds.close()
    except:
        print 'Seed file is yet empty!'
    register_seed(seed)
    return seed

def shuffle_scale(lower, upper):
    seed = create_seed()
    rnd = random.Random(seed)
    tidy = init_list(lower, upper)
    def return_shuffle(array):
        rnd.shuffle(array)
        str_array = str(array)[1:-1]
        return str_array
    orderings = []
    #header, redundant
    orderings.append(filename[:-3] + str(default_amount) + str(seed))
    for i in range(0, default_amount,1):
        orderings.append(return_shuffle(tidy))
    return orderings

def GetExtSrcDataDjangoPK():
    return External_Source_Data.objects.count() + 1

def GetOrderDjangoPK():
    global order_counter
    order_counter += 1
    return order_counter

def write_json(rnd_orderings):
    #writes a list to json

    #parent 
    #subs: pk, fields
    ext_source_data = '{"model":"eyevacs.External_Source_Data","pk":"%s","fields":%s}'
    #subs: header expname expid
    ext_source_data_fields = '{"filetye":"scale","header":"%s","exp_name":"%s","experiment":"%s"}'
    output = '[%s, %s]'
    pk = GetExtSrcDataDjangoPK()
    fields_content = (filename[:-6], experiment_name, experiment_id)
    data = ext_source_data % (pk, (ext_source_data_fields % fields_content))

    output = open(fixture_path + filename,'w')
    output.write('[')
    output.write(data)

    #children
    #pk # fields
    rnd_frame = '{"model":"eyevacs.External_Order_Scale","pk":"%s","fields":%s}'
    #i # str(ordering)
    rnd_fields = '{"id_hard":"%s","scale_rnd_order_ext":"%s","linked_pcpt":"null"}'
    for i in range(1,len(rnd_orderings),1):
        pk = GetOrderDjangoPK()
        rnd_content = (i, rnd_orderings[i])
        line = rnd_frame % (pk, (rnd_fields % rnd_content))
        output.write(',\n')
        output.write(line)
    output.write(']')
    output.close()
    print ' -- Created ###' + filename + '### under:\n ### ' + data_path + '### --'

def LowerInput():
    try:
        lower = int(raw_input('Lower limit:\n'))
        return lower
    except:
        print 'INTEGER only!'
        LowerInput()

def UpperInput():
    try:
        upper = int(raw_input('Upper limit:\n'))
        return upper
    except:
        print 'INTEGER only!'
        UpperInput()

#def main(ext_data_path, exp_id):
def main(exp_id):
    global data_path
    global fixture_path
    global experiment_name
    global experiment_id
    global filename
    global seedname
    global order_counter
    exp = Experiment.objects.get(pk=exp_id)
    experiment_name = exp.name
    current_exp_id = exp.pk
    #data_path = ext_data_path
    data_path = './eyevacs/data/' + experiment_name + '/'
    fixture_path =  './eyevacs/fixtures/' + experiment_name + '/'
    print 'exp od', exp_id
    experiment_id = exp_id
    order_counter = External_Order_Scale.objects.count()
    name = raw_input('Enter Name of Order (Scales name):\n')
    print name
    seedname = 'SEED_%s.csv' % name
    filename = 'RND_%s.json' % name
    lower = LowerInput()
    upper = UpperInput()
    untidy = shuffle_scale(lower, upper) #includes header with its seed
    write_json(untidy)

if __name__ == '__main__':
    import sys
    args = sys.argv
    main(args[1],args[2])
'''
execfile('./scripts/create_rnd_scale.py')
main(1)
'''
