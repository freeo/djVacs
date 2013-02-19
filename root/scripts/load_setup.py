from eyevacs.models import Experiment, Attribute, Level

attributes = ['catering','customer rating', 'type of building', 'sea view', 'price', 'room category']

#index is used for for its VALUE! Higher values are expected to be beneficial
levels = {'catering':['breakfast only', 'half board', 'all-inclusive'],'customer rating':['low','medium','high'], 'type of building':['bungalow','rooming house', 'hotel complex'], 'sea view':['no sea view','side sea view','full sea view'], 'price':['499$','399$','299$'], 'room category':['standard','superior','deluxe']}

positions = {'catering':1,'customer rating':2, 'type of building':3, 'sea view':4, 'price':5, 'room category':6}


def getPosition(key):
    return positions[key]

def main(exp):
    print ' ---  writing static Attributes & Levels... ---'
    for key in levels.keys():
        level_list = levels[key]
        newname = key
        newposition = getPosition(key)
        newAttribute = Attribute(name = newname, exp_setup = exp, position = newposition)
        newAttribute.save()
        for level in level_list:
            lvlname = level
            lvlvalue = level_list.index(level)
            newlevel = Level(link_attribute = newAttribute, name = lvlname, value = lvlvalue)
            newlevel.save()
    print ' ----------------------------------------------------------------------'
    print ' --- Static Attributes & Levels are saved to Experiment: ',exp.name, ' ---'
    print ' ----------------------------------------------------------------------'

