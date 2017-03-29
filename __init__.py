try:
    import os
    import sys
    import datetime
    import subprocess
except ImportError as e:
    raise e


def help_inf():
    """
        ______ __   __                 _             
       / ____// /_ / /_   ___   _____ (_)__  __ _____       _   __     ______      __
      / __/  / __// __ \ / _ \ / ___// // / / // ___/      | | / /    / __  /     / /
     / /___ / /_ / / / //  __// /   / // /_/ /(__  )       | |/ /    / /_/ / __  / /
    /_____/ \__//_/ /_/ \___//_/   /_/ \__,_//____/        |___/    /_____/ /_/ /_/
                                                 
    """
    pass


def path_to(main_path, *args):
    for name in args:
        sys.path.append(os.path.join(name))
        # print()
    return 0

__version__ = '0.1'
os_name = sys.platform

if __name__ == '__main__':
    os.system('clear')
    print(help_inf.__doc__)
    print()
    print('{0}\tEtherius automatisation complex. Version = {1}'.format(datetime.datetime.now(), __version__))

main_path = (str(os.path.realpath(os.path.dirname(sys.argv[0]))))
print('{0}\tApplication configuring'.format(datetime.datetime.now()))
path_to(main_path,
        'src',
        'src/dwld',
        'sh',
        'cfg',
        'src/cmd',
        )

if os_name == 'linux':
     subprocess.call(['bash', 'sh/module_import.sh'])
try:
    import shell
except ImportError as e:
    print('{0}\tCannot loading main module.'.format(datemite.datetime.now()))
    raise e