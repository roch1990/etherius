import sys, os

path_to_bin = (str(os.path.realpath(os.path.dirname(sys.argv[0]))) + '\BIN')
sys.path.append(path_to_bin)

command = 'help'

while command != 'exit':
    if command == 'help':
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
    if command == 'GPS_load':
        import GPSDownloader
    if command == 'GLO_load':
        import GLONASSDownloader
    if command == 'BULL_load':
        import BULLET_AERPDownloader
    if command == 'SATORB':
        import SATORB
    if command == 'anMAXIS':
        import MAXIS_analyzer
    if command == 'anNODE':
        import NODE_analyzer
    if command == 'anINCL':
        import INCLANATION_analyzer
    if command == 'anPER':
        import PERIGEE_analyzer
    if command == 'anECC':
        import ECCENTRICITY_analyzer
    command = input()
else:
    print('Thank you for using this programm!')
    input('Press Enter to quit')
    sys.exit







