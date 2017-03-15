import sys, os

def  path_to(main_path, *args):
    for name in args:
        sys.path.append(main_path + '/' + name)
        print(main_path + '/' + name)
    return 0

def  command_init(name):
    """Function for input command processing"""
    if name == 'info':
        print('\nHello and welcome to automatisation of Celestial Mechanics programm!\n')
        print('You can use this comands in shell:')
        print('info - if you need to read help information')
        print('GPS_load - if you need to download a GPS ephemeris')
        print('GLO_load - if you need to download a GLONASS ephemeris')
        print('BULL_load - if you need to update your BULLET_A.erp file')
        print('SATORB - computation with SATORB utility')
        print('anMAXIS - if you need to get major axis from *.OUT file')
        print('anECC - if you need to get eccentricity from *.OUT file')
        print('anINCL - if you need to get inclanation from *.OUT file')
        print('anNODE - if you need to get r.a.node from *.OUT file')
        print('anPER - if you need to get a.o.perigee from *.OUT file')
        print('exit - if you want to quit\n')
    elif name == 'GPS_load':
        import gps_eph_dwld
    elif name == 'GLO_load':
        import glo_eph_dwld
    elif name == 'BULL_load':
        import earth_param_dwld
    elif name == 'SATORB':
        import satorb_aut
    elif name == 'anMAXIS':
        import max_anlz
    elif name == 'anNODE':
        import node_anlz
    elif name == 'anINCL':
        import incl_anlz
    elif name == 'anPER':
        import prg_anlz
    elif name == 'anECC':
        import ecc_anlz
    else:
        print('Wrong command string. Type \"info\" for help')
    return 0
 

main_path = (str(os.path.realpath(os.path.dirname(sys.argv[0]))))
print('Adding directory to sys path:')
path_to(main_path, 'src/deph', 'src/anlz', 'src/satorb')

command = 'info'   

while command != 'exit':
    command_init(command)
    command = input()
else:
    print('Thank you for using this programm!')
    input('Press Enter to quit')
    sys.exit