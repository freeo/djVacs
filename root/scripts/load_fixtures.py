import os
from subprocess import call
import sys

#paths
root_path = ''
fixture_path = ''

def Run(root, fixtures):
    global fixture_path
    global root_path
    fixture_path = fixtures
    root_path = root
    Main()

def Main():
    current_wd = os.getcwd()
    os.chdir(root_path + fixture_path)
    file_list = os.listdir('.')
    cmd_template = [sys.executable, root_path + '/manage.py', 'loaddata']
    print fixture_path
    print 'Found '+str(len(file_list))+' files: \n'
    for fixture in file_list:
        print fixture + ' --- installing...'
        cmd_template.append(fixture)
        call(cmd_template, shell=True)
        cmd_template.pop()
        print fixture , ' was installed successfully!'
    os.chdir(current_wd)

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


