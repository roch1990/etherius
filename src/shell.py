import sys
import os
import datetime


def help_inf():
    """          API interface
    prefix | type   |  method | key | value
    _______|________|_________|_____|______
    config |etherius| get     |stage| key
           |glonass | set     |     |
           |gps     |         |     |
    load   |glonass |raw      |alma |
           |gps     |         |eph  |rapid
           |        |         |     |final
           |        |         |stat |const
           |        |         |     |stark
           |        |         |brdc |
           |        |         |bull |daily
           |        |         |     |weekly
           |        |         |     |monthly
    analyze|glonass |         |     |
           |gps     |         |     |
    exit   |        |         |     |
    """
    return True


def command_validation(command, arg_num):
    """Command validation function"""
    # print('comm validation: {0}, arg number: {1}'.format(command, arg_num))
    if command == 'config' and arg_num != 5:
        print('{0}\tCommand argument error'.format(datetime.datetime.now()))
        print('{0}\tYou entered {1} arguments. Expected 5'.format(datetime.datetime.now(), arg_num))
        return False
    else:
        return True
    if command == 'load' and arg_num < 4:
        print('{0}\tCommand argument error'.format(datetime.datetime.now()))
        print('{0}\tYou entered {1} arguments. Expected 5'.format(datetime.datetime.now(), arg_num))
        return False
    else:
        return True


def config_gs(command):
    """Load parameters from config file"""
    import eth_cfg_loader
    # print('Config load: {}'.format(command))
    if command_validation(command[0], len(command)):
        param = command[1]
        method = command[2]
        key = command[3]
        value = command[4]
        # print(eth_cfg_loader.get_inf(param, key, value))
        return eth_cfg_loader.get_inf(param, key, value)
    else:
        return False


def load(command):
    loader = []
    try:
        import loader
    except ImportError as e:
        print('{0}\t{1}'.format(datetime.datetime.now(), e))
    if  command[3] == 'alma':
        param = loader.load_alma(command)
        # print(param)
        import alma_ftp_dwld
        alma_ftp_dwld.ftp_worker(data_format=param[0],
                                 path=param[1],
                                 idate=param[2],
                                 edate=param[3],)
    else:
        print('Command line internal error!')
    return True

command = ['']

while command[0] != 'exit':
    command = input('>> ').split(' ')
    if command[0] == 'config':
        config_gs(command)
    elif command[0] == 'load':
        load(command)
    elif command[0] == 'help':
        print(help_inf.__doc__)
else:
    print('Thank you for using this programm!')
    input('Press Enter to quit')
    sys.exit
