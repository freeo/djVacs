from scripts import load_fixtures
import os
import sys

#paths
root = sys.path[0]
external_data_path = '/external_data/'
fixture_output = '/eyevacs/fixtures/'

def __main__():
    print 'starting...'
    load_fixtures.Run(root, fixture_output)

if __name__ == "__main__":
    __main__()
