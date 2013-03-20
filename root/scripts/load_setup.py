from eyevacs.models import Experiment, Attribute, Level

attributes = ['food quality','customers recommending', 'distance to CBD', 'sea view', 'price per person', 'room category']

#index is used for for its VALUE! Higher values are expected to be beneficial
levels = {'food quality':['good', 'very good', 'excellent'],'customers recommending':['50%','70%','90%'], 'distance to CBD':['3 km','2 km', '1 km'], 'sea view':['no sea view','side sea view','full sea view'], 'price per person':['$899','$799','$699'], 'room category':['standard','superior','deluxe']}

positions = {'food quality':1,'customers recommending':2, 'distance to CBD':3, 'sea view':4, 'price per person':5, 'room category':6}


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

