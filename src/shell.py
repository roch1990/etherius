import sys, os

def  path_to(main_path, *args):
    for name in args:
        sys.path.append(main_path + '/' + name)
        print(main_path + '/' + name)
    return 0

def  command_init(name):
    """Function for input command processing"""
    if name == 'help':
        print('Hello and welcome to automatisation of Celestial Mechanics programm!')
        print()
        print('You can use this comands in shell:')
        print('help - if you need to read help information')
        print('GPS_load - if you need to download a GPS ephemeris')
        print('GLO_load - if you need to download a GLONASS ephemeris')
        print('BULL_load - if you need to update your BULLET_A.erp file')
        print('SATORB - computation with SATORB utility')
        print('anMAXIS - if you need to get major axis from *.OUT file')
        print('anECC - if you need to get eccentricity from *.OUT file')
        print('anINCL - if you need to get inclanation from *.OUT file')
        print('anNODE - if you need to get r.a.node from *.OUT file')
        print('anPER - if you need to get a.o.perigee from *.OUT file')
        print('exit - if you want to quit')
        print()
    if name == 'GPS_load':
        import gps_eph_dwld
    if name == 'GLO_load':
        import glo_eph_dwld
    if name == 'BULL_load':
        import earth_param_dwld
    if name == 'SATORB':
        import satorb_aut
    if name == 'anMAXIS':
        import max_anlz
    if name == 'anNODE':
        import node_anlz
    if name == 'anINCL':
        import incl_anlz
    if name == 'anPER':
        import prg_anlz
    if name == 'anECC':
        import ecc_anlz
    return 0
 

main_path = (str(os.path.realpath(os.path.dirname(sys.argv[0]))))
print('Adding directory to sys path:')
path_to(main_path, 'src/deph', 'src/anlz', 'src/satorb')

command = 'help'   

while command != 'exit':
    command_init(command)
    command = input()
else:
    print('Thank you for using this programm!')
    input('Press Enter to quit')
    sys.exit