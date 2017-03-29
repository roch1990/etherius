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
    raise e


def get_config_data(param, stage, key):
    # import module for *.cfg file parsing
    if param == 'eth':
        cfg_file = os.path.join(os.path.abspath(os.curdir),'cfg', 'etherius.cfg')
    elif param == 'glo':
        cfg_file = os.path.join(os.path.abspath(os.curdir),'cfg', 'glonass.cfg')
    elif param == 'gps':
        cfg_file = os.path.join(os.path.abspath(os.curdir),'cfg', 'gps.cfg')
    eth_config = configparser.ConfigParser()
    try:
        eth_config.read(cfg_file)
        return eth_config.get(str(stage), str(key))
    except Exception as e:
        print('{0}\tCannot load config file. Error: {1}'.format(datetime.datetime.now(), e))
        return False


def param_convert(param):
    param_dict = dict(glonass='glo',
                      gps='gps',
                      etherius='eth',
                      almanac='alma',
                      status='stat',
                      brdc='brdc',
                      products='prod',
                      bulletin='bull',
                      gormat='form',)
    param = param_dict[param]
    return param


def get_inf(param, key, value):
    """Return data from config file"""
    # converting command to samll param
    param = param_convert(param)
    # command = param_convert(value)
    return get_config_data(param, key, value)
