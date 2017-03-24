import os, sys,datetime

def  path_to(main_path, *args):
    for name in args:
        sys.path.append(main_path + '/' + name)
        #print(main_path + '/' + name)
    return 0

__version__ = '0.1'
os_name = sys.platform

if __name__ == '__main__':
     print('{0}\tEtherius automatisation complex. Version = {1}'.format(datetime.datetime.now(), __version__))
          
main_path = (str(os.path.realpath(os.path.dirname(sys.argv[0]))))
print('{0}\tApplication configuring'.format(datetime.datetime.now()))
path_to(main_path,
        'src',
        'src/dwld',
        'sh',
        'cfg',
        )

if os_name == 'linux':
     import subprocess
     subprocess.call(['bash', 'sh/module_import.sh'])

import shell