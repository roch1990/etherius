'''
Module for application configuration
Module represented this logic:
summary input:
    input: param(etherius, glonass, gps), stage(config type), data_key(key)
    output: value
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
try:
    import datetime
    import os
    import configparser
except ImportError as e:
    print(e)


def get_config_data(param, stage, key):
    # import module for *.cfg file parsing
    if param == 'eth':
        cfg_file = os.path.abspath(os.curdir) + '/cfg/etherius.cfg'
    elif param == 'glo':
        cfg_file = os.path.abspath(os.curdir) + '/cfg/glonass.cfg'
    elif param == 'gps':
        cfg_file = os.path.abspath(os.curdir) + '/cfg/gps.cfg'
    eth_config = configparser.ConfigParser()
    try:
        eth_config.read(cfg_file)
        return eth_config.get(str(stage), str(key))
    except NameError as e:
        print(e)
        return False


def stage_validation(param, stage):
    if param == 'eth':
        stage_range = ['data_path', 'eph_type', 'bull_type',
                       'frc_type', 'stat_param', 'data_type']
    elif param in ['glo', 'gps']:
        stage_range = ['init_date', 'endp_date']
    else:
        print('{0}\tParameter validation error:\t{1}'.format(datetime.datetime.now(), param))
        return False
    if stage in stage_range:
        return True
    else:
        print('{0}\tSection validation error:\t{1}'.format(datetime.datetime.now(), stage_range))
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
    elif param in ['glo', 'gps']:
        key_range = ['year', 'month', 'day', 'hour']
    else:
        print('{0}\tParameter validation error:\t{1}'.format(datetime.datetime.now(), param))
        return False
    if key in key_range:
        return True
    else:
        print('{0}\tKey validation error:\t{1}'.format(datetime.datetime.now(), key))
        return False


def inp_validations(param, stage, key):
    # summary result of validations
    return stage_validation(param, stage) & key_validation(param, key)


def param_convert(param):
    if param == 'glonass':
        param = 'glo'
    elif param == 'gps':
        param = 'gps'
    elif param == 'etherius':
        param = 'eth'
    elif param == 'almanac':
        param = 'alma'
    elif param == 'status':
        param = 'stat'
    elif param == 'brdc':
        param = 'brdc'
    elif param == 'products':
        param = 'prod'
    elif param == 'bulletin':
        param = 'bull'
    elif param == 'format':
        param = 'form'
    else:
        param = ''
    return param


def get_inf(param, key, value):
    """Return data from config file"""
    # converting command to samll param
    param = param_convert(param)
    # command = param_convert(value)
    # validations
    if inp_validations(param, key, value):
        # result
        return get_config_data(param, key, value)
    else:
        return inp_validations(param, key, value)
