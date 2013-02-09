stringlist = 'abcdefgh lalala a0woijef'
liste = stringlist.split()
print liste
print liste.index('lalala')
'''
import os
import re
# here() gives us file paths from the root of the system to the directory
# holding the current file.
here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

PROJECT_ROOT = here("..")
# root() gives us file paths from the root of the system to whatever
# folder(s) we pass it starting at the parent directory of the current file.
root = lambda * x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)
print root(here())
print root()
print here()
#print str(re.sub('\\', '/', temp))

'''
'''
print 'stuff'
stra = 'asdf'
aa= []
aa.app
'''
'''
org ='E:\djVacs\root./external_data/'
r1 = 'E:\djVacs\root/external_data/'
r2 = 'E:\\djVacs\\root/external_data/'
asf = 'astupidfile.asf'
f = open(r2+asf,'w')
f.write('ololol')
f.close()
'''

'''import os
folder = './new folder/'
filename = 'myfile.py'
if os.path.isdir(folder):
    f= open(folder + filename,'w')
    f.write('print writing another line...')
else:
    os.makedirs(folder)
    f= open(folder + filename,'w')
    f.write('print writing another line...')
f.close()
'''

'''
#random mersenne twister generation
import random

rnd1 = random.Random()
rnd1.seed(20125)
print rnd1.uniform(7,16)

rnd2 = random.Random()
rnd2.seed(20126)
print rnd2.uniform(7,16)

ls = [1,2,3,4,5,6,7,8,9]

lstr = str(ls)
renew = map(int, lstr[1:-1].split(','))

print lstr[1:-1]
print renew

anew = []
#rnd1.shuffle(ls, anew)
print 'segsegseg\n\n\n'
print anew
print ls
print 'segsegseg\n\n\n'
rnd1.shuffle(ls)
print ls
rnd1.shuffle(ls)
print ls
rnd1.shuffle(ls)
print ls
'''

'''
#calling a script with arguments

from subprocess import call
import os
import sys

print os.getcwd()
dirlist = os.listdir('.')
print dirlist

args = ['abc','def','ghi']
args2 =['jkl','mno','pqr']
call([sys.executable,'ext.py']+args+args2, shell=True)

#content of ext.py
import sys

print 'helloo'

for arg in sys.argv:
    print arg

for index, arg in enumerate(sys.argv):
    print index, arg

'''

"""
#calling a batch file
import os
import subprocess

print os.getcwd()
output_path ='../eyevacs/fixtures/'
os.chdir(output_path)
print os.getcwd()
print output_path + 'batch.bat'
subprocess.call(['batch.bat'])
"""

'''
#DEPRECATED executing external commands with os.system
import os

output_path ='../eyevacs/fixtures/'
root = ''

os.chdir(output_path)
dirlist = os.listdir('.')
print dirlist

batch = open('batch.bat', 'w')
cmds = 'echo hallo welt!\nPAUSE'
batch.write(cmds)
batch.close()

os.system('batch.bat')
'''



'''
#deadly nested triple adressing
# Explanation
#iterators = (i,j,k)
#maximum values = (I,J,K)
#index = i*J*K+j*K+k+1
#bigger! with l and L:
#iJKL+jKL+kL+l+1

total_tasks = 2
bsl_max_cts = 21
for i in range(0, int(total_tasks),1):
    for j in range (0,bsl_max_cts,1):
        index = ''
        for k in range(0,5,1):
            index += str(i*bsl_max_cts*5+j*5+k+1) + ',' #skipping header
        print index
        print 'k end'
    print 'j end \n'
print 'i end \n'
'''

'''
rawHeader = '"kulu","hala","bele","","bisi"'
print rawHeader.replace('"','')
'''

'''az = "abc %s cde %s fgh %s ijk %s lmn %s"
h1 = 'hihi'
h2 = ('hi','hihi')
h3 = ('hi','hihi','hihihi')
h5 = ('hi','hihi','hihihi','ho','hoho')
#print az
print h2 + h3
print az % h2 + h3
'''

'''
mylist = [None]*8
print mylist
mylist[5]=5
print mylist
'''

'''
import datetime

def unix_time(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    delta = dt - epoch
    return delta.total_seconds()

def unix_time_millis(dt):
    return unix_time(dt) * 1000.0

atime = unix_time_millis(datetime.datetime.utcnow())
print atime
#print datetime.datetime.utcfromtimestamp(atime)
#print datetime.datetime.utcnow()

print len(str(atime))

print 17*18+17
'''
