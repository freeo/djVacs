import random
import os
from eyevacs.models import Experiment, External_Source_Data, External_Order_Scale

data_path = ''
fixture_path = ''
seedname = ''
filename = ''
init_list = []
default_amount = 900
experiment_name = ''
experiment_id = None
rnd_counter_db = None
rnd_counter_file = None
rnd_counter_running = None
#order_counter = None
#internal_order_counter = None
order_counter_db = None
order_counter_file = None
order_counter_running = None
#internal_extdata_counter = None

def init_list(lower, upper):
    output = []
    for i in range(lower, upper+1, 1):
        output.append(i)
    return output

def initIDs():
    global rnd_counter_db
    global rnd_counter_file
    global rnd_counter_running
    global order_counter_db
    global order_counter_file
    global order_counter_running
    order_counter_db = External_Source_Data.objects.count()
    rnd_counter_db = External_Order_Scale.objects.count()
    try:
        f = open(data_path + 'temp_IDcount.csv', 'r')
        internal_counters = f.readline().split(';')
        order_counter_file = int(internal_counters[0])
        rnd_counter_file = int(internal_counters[1])
        f.close()
    except:
        print 'EXCEPT IDcount'
        f = open(data_path + 'temp_IDcount.csv', 'w')
        f.write('0;0')
        order_counter_file = 0
        rnd_counter_file = 0
        f.close()
    order_counter_running = 0
    rnd_counter_running = 0
    print 'IDs initialized!'
    print 'data source: ',order_counter_db,order_counter_file, order_counter_running
    print 'order scale: ',rnd_counter_db, rnd_counter_file, rnd_counter_running

def register_seed(seed):
    used_seeds = open(data_path + seedname, 'a')
    used_seeds.write(filename[:-5])
    used_seeds.write('\n')
    used_seeds.write(str(seed)+'\n')
    used_seeds.close()

def init_seed_file():
    try:
        used_seeds = open(data_path + seedname, 'r')
    except:
        used_seeds = open(data_path + seedname, 'w')
    used_seeds.close()


def create_seed():
    seed = random.randint(100000,999999)
    seeds = []
    init_seed_file()
    used_seeds_file = open(data_path + seedname, 'r')
    used_seeds = used_seeds_file.readlines()
    used_seeds_file.close()
    #print 'length', len(used_seeds)
    for i in range(0,len(used_seeds),1):
        seeds.append(used_seeds[i])
        try:
            if int(seeds[i]) == seed:
                create_seed()
                break
        except:
            #no shit sherlock
            print '-- no seed duplicate -- '
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


def GetOrderDjangoPK():
    global rnd_counter_running
    rnd_counter_running += 1
    freePK = rnd_counter_db + rnd_counter_file + rnd_counter_running
    #freePK = internal_extdata_counter + External_Source_Data.objects.count() + 1
    #internal_extdata_counter = freePK
    return freePK

def GetExtSrcDataDjangoPK():
    global order_counter_running
    order_counter_running += 1
    freePK = order_counter_db + order_counter_file + order_counter_running
    return freePK

def write_json(rnd_orderings):
    #writes a list to json

    #parent 
    #subs: pk, fields
    ext_source_data = '{"model":"eyevacs.External_Source_Data","pk":"%s","fields":%s}'
    #subs: header expname expid
    ext_source_data_fields = '{"filetype":"scale","header":"%s","exp_name":"%s","experiment":"%s"}'
    output = '[%s, %s]'
    pk = GetExtSrcDataDjangoPK()
    fields_content = (filename[:-5], experiment_name, experiment_id)
    data = ext_source_data % (pk, (ext_source_data_fields % fields_content))

    output = open(fixture_path + filename,'w')
    output.write('[')
    output.write(data)

    #children
    #pk # fields
    rnd_frame = '{"model":"eyevacs.External_Order_Scale","pk":"%s","fields":%s}'
    #i # str(ordering)
    rnd_fields = '{"id_hard":"%s","scale_rnd_order_ext":"%s","linked_pcpt":null}'
    for i in range(1,len(rnd_orderings),1):
        pk = GetOrderDjangoPK()
        rnd_content = (i, rnd_orderings[i])
        line = rnd_frame % (pk, (rnd_fields % rnd_content))
        output.write(',\n')
        output.write(line)
    output.write(']')
    output.close()
    print ' -- Created *' + filename + '* under:\n ### ' + data_path + ' ### --'

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



def writeInternalIDs():
    f = open(data_path + 'temp_IDcount.csv', 'w')
    internal_counters = []
    internal_counters.append(order_counter_file + order_counter_running)
    internal_counters.append(rnd_counter_file + rnd_counter_running)
    f.write(str(internal_counters[0]) + ';' + str(internal_counters[1]))
    f.close()

#def main(ext_data_path, exp_id):
def main(exp_id, args=('',None,None)):
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
    experiment_id = exp_id
    seedname = 'SEED_%s.csv' % experiment_name
    if args == ('',None,None):
        name = raw_input('Enter Name of Order (Scales name):\n')
        lower = LowerInput()
        upper = UpperInput()
        while lower >= upper:
            print 'Wrong input! Lower has to be greater then Upper!'
            lower = LowerInput()
            upper = UpperInput()
    else:
        name = args[0]
        lower = args[1]
        upper = args[2]
    initIDs()
    this_id = order_counter_db + order_counter_file + order_counter_running
    filename = 'RND_id%s_%s.json' % (this_id,name)
    untidy = shuffle_scale(lower, upper) #includes header with its seed
    write_json(untidy)
    writeInternalIDs()

'''
if __name__ == '__main__':
    import sys
    args = sys.argv
    main(args[1],args[2])

execfile('./scripts/create_rnd_scale.py')
main(1)
'''
