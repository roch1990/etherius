try:
    import sys
    import os
    import datetime
    import cmd_valid
    import eth_cfg_loader
    import loader
    import alma_ftp_dwld
except ImportError as e:
    raise e


def help_inf():
    """          API interface
    prefix | type   |  method | key | value
    _______|________|_________|_____|______
    config |etherius| get     |stage| key
           |glonass | set     |     |
           |gps     |         |     |
    load   |glonass |raw      |alma |none
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


def config_gs(command):
    """Load parameters from config file"""
    # print('Config load: {}'.format(command))
    if cmd_valid.command_validation(command, len(command)):
        param = command[1]
        method = command[2]
        key = command[3]
        value = command[4]
        # print(eth_cfg_loader.get_inf(param, key, value))
        return eth_cfg_loader.get_inf(param, key, value)
    else:
        return False


def load(command):
    # command validation
    if cmd_valid.command_validation(command, len(command)):
        if  command[3] == 'alma':
            param = loader.load_alma(command)
            # print(param)
            alma_ftp_dwld.ftp_worker(data_format=param[0],
                                     path=param[1],
                                     idate=param[2],
                                     edate=param[3],)
        return True
    else:
        return False

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
