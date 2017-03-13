import os, sys

__version__ = '0.1'

if __name__ == '__main__':
     print('Etherius automatisation complex. Version = ' + __version__)

main_path = (str(os.path.realpath(os.path.dirname(sys.argv[0]))) )
sys.path.append(main_path + '/src')

import shell