import os
from subprocess import call
import sys

#paths
root_path = ''
fixture_path = ''
data_path = ''

def Run(root, fixtures, data):
    global fixture_path
    global root_path
    global data_path
    fixture_path = fixtures
    root_path = root
    data_path = data
    Main()

def Main():
    current_wd = os.getcwd()
    print current_wd
    print root_path + fixture_path
    os.chdir(root_path + fixture_path)
    print 'new wd'
    print os.getcwd()

    file_list = os.listdir('./')
    cmd_template = [sys.executable, current_wd + '\\manage.py', 'loaddata']

    print 'Found '+str(len(file_list))+' files: \n'
    print file_list, '\n'
    for fixture in file_list:
        print fixture + ' --- installing...'
        cmd_template.append(fixture)
        #print  cmd_template
        call(cmd_template, shell=True)
        cmd_template.pop()
        print fixture , ' was installed successfully!'
    os.chdir(current_wd)
    try:
        os.remove(root_path + data_path + 'temp_IDcount.csv')
        print '--- temporary ID counts have been resetted! ---'
    except:
        print '--- File "temp_IDcount.csv" doesnt exist! ---'

if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) < 2:
        print '***'
        print 'Aborted. Missing Arguments. Append the following arguments:'
        print 'load_fixtures (root path) (path to fixtures)'
        print '***'
    else:
        root = args[0]
        fixture_path = args[1]
        Main()


