import sys, os, datetime

def __doc__():
    """
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
    print(__doc__)
    return 1

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
    # print('Command load: {}'.format(command))
    # external dictionary for dwld operations
    cfg_request = ['config', 'etherius', 'get']
    date_list = ['year', 'month', 'day', 'hour']
    idate = []
    edate = []
    param = []
    # choose config command for cfg 
    if command[1] == 'glonass':
        idate_request = ['config', 'glonass', 'get', 'init_date']
        edate_request = ['config', 'glonass', 'get', 'endp_date']
        alma_stage = dict(data_path  = 'alma',
                          data_type = 'glo_alma',)
    elif command[1] == 'gps':
        idate_request = ['config', 'gps', 'get', 'init_date']
        edate_request = ['config', 'gps', 'get', 'endp_date']
        alma_stage = dict(data_path  = 'alma',
                          data_type  = 'gps_alma',)
    #returninig of init date and end date
    for item in date_list:
        idate_request.append(item)
        idate.append(config_gs(idate_request))
        edate_request.append(item)
        edate.append(config_gs(edate_request))
        idate_request.pop()
        edate_request.pop()
    # print('Initial date: {0}\nEndpoint date: {1}'.format(idate, edate))
    # returning of
    for item in alma_stage.keys():
        cfg_request.append(item)
        cfg_request.append(alma_stage.get(item))
        param.append(config_gs(cfg_request))
        cfg_request.pop()
        cfg_request.pop()
    param.append(idate)
    param.append(edate)
    print(param)
    import ftp_dwld
    ftp_dwld.ftp_worker(data_format = param[0],
                        path  = param[1],
                        idate = param[2],
                        edate = param[3],
                        )
    return True

command = ['']

while command[0] != 'exit':
    command = input('>> ').split(' ')
    if command[0] == 'config':
        config_gs(command)
    elif command[0] == 'load':
        load(command)
else:
    print('Thank you for using this programm!')
    input('Press Enter to quit')
    sys.exit