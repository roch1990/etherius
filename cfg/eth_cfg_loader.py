'''
Module for application configuration
Module represented this logic:
get_inf -> validations -(if ok) -> get_config_data
get_inf:
    input  = param, stage, key (string)
    output = get_config_date (string)
get_config_date:
    input: param, stage, key (string)
    output: value (string)
stage_validation:
    input: param, stage (string)
    output: result of stage name validation (bool)
key_validation:
    input: param, key (string)
    output: result of key name validation (bool)
inp_validation:
    input: param (string), stage_validation, key_validation (bool)
    output: summary of key and stage validation (bool)
'''

def get_config_data(param, stage, key):
    # import module for *.cfg file parsing
    import os
    if param == 'eth':
        cfg_file = os.path.abspath(os.curdir) + '/cfg/etherius.cfg'
    elif param == 'glo':
        cfg_file = os.path.abspath(os.curdir) + '/cfg/glonass.cfg'
    elif param == 'gps':
        cfg_file = os.path.abspath(os.curdir) + '/cfg/gps.cfg'
    import configparser
    eth_config = configparser.ConfigParser()
    try:
       eth_config.read(cfg_file)
       return eth_config.get(str(stage), str(key))
    except NameError as e:
        print(e)
        return -1    

def stage_validation(param, stage):
    if param == 'eth':
        stage_range = ['data_path', 'eph_type', 'bull_type',
                     'frc_type', 'stat_param', 'data_type']
    elif param == ('glo' or 'gps'):
        stage_range = ['init_date', 'endp_date']
    else:
        return False
    if stage in stage_range:
        return True
    else:
        return False
    
def key_validation(param, key):
    if param == 'eth':
        key_range = ['root', 'alma', 'stat', 'brdc', 'prod', 'bull', 'form',
                     'rapid', 'final',
                     'daily', 'weekly', 'monthly', 
                     'none', 'last24', 'forecast0006', 'forecast0612', 'forecast1218', 'forecast1824',
                     'const', 'stark',
                     'gps_alma', 'glo_alma', 'gps_stat', 'glo_stat', 'sat_hlth',
                     'glo_rinx', 'gps_rinx', 'sat_ephm', 'sat_clck', 'sat_bull']
    elif param == ('glo' or 'gps'):
        key_range = ['year', 'month', 'day']
    else:
        return False
    if key in key_range:
        return True
    else:
        return False

def inp_validations(param, stage, key):
    #summary result of validations
    return stage_validation(param, stage) & key_validation(param, key)

def get_inf(param, stage, command):
    # converting command to small param
    if param == 'glonass':
        param = 'glo'
    elif param == 'gps':
        param = 'gps'
    elif param == 'etherius':
        param = 'eth'
    # converting command to small param
    if command == 'almanac':
        command = 'alma'
    elif command == 'status':
        command = 'stat'
    elif command == 'brdc':
        command = 'brdc'
    elif command == 'products':
        command = 'prod'
    elif command == 'bulletin':
        command = 'bull'
    elif command == 'format':
        command = 'form'
    #validations    
    if inp_validations(param, stage, command):
        #result 
        return get_config_data(param, stage, command)
    else:
        return inp_validations(param, stage, command)