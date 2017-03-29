try:
    import datetime
except ImportError as e:
    raise e


def internal_validation(param, value_list):
    if param in value_list:
        return True
    else:
        print('{0}\tComand line error. Invalid parameter: {1}'.format(datetime.datetime.now(), param))
        return False


def load_valid(command):
    c_type = ('gps',
              'glonass',)
    c_method = ('raw',)
    c_key = ('alma',
             'eph',
             'stat',
             'brdc',
             'bull',)
    c_value = ('none',
               'rapid',
               'final',
               'const',
               'stark',
               'daily',
               'weekly',
               'monthly',)
    return internal_validation(command[1], c_type) and \
           internal_validation(command[2], c_method) and \
           internal_validation(command[3], c_key) and \
           internal_validation(command[4], c_value)


def cfg_validation(command):
    c_type = ('etherius', 'glonass', 'gps')
    c_method = ('get', 'set')
    return internal_validation(command[1], c_type) and \
           internal_validation(command[2], c_method)


def command_validation(command, arg_num):
    """Simple command validation function"""
    # print('comm validation: {0}, arg number: {1}'.format(command, arg_num))
    if (command[0] == 'config' and arg_num == 5):
        # print('{0}\tConfig command Ok'.format(datetime.datetime.now()))
        return (True and cfg_validation(command))
    elif (command[0] == 'load' and arg_num == 5):
        return (True and load_valid(command))
    else:
        print('{0}\tCommand argument error'.format(datetime.datetime.now()))
        print('{0}\tYou entered {1} arguments. Expected 5'.format(datetime.datetime.now(), arg_num))
        return False
