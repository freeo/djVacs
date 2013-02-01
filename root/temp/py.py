

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
