import os, sys

def  path_to(main_path, *args):
    for name in args:
        sys.path.append(main_path + '/' + name)
        print(main_path + '/' + name)
    return 0

__version__ = '0.1'
os_name = sys.platform

if __name__ == '__main__':
     print('Etherius automatisation complex. Version = ' + __version__)
          
main_path = (str(os.path.realpath(os.path.dirname(sys.argv[0]))))
print('Adding directory to sys path:')
path_to(main_path, 'src', 'src/deph', 'sh', 'cfg')

if os_name == 'linux':
     import subprocess
     subprocess.call(['bash', 'sh/module_import.sh'])

import shell