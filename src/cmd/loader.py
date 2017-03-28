try:
    import shell
except Exception as e:
    raise e


def load_alma(command):
    # print('Command load: {}'.format(command))
    # commands for config requests
    cfg_request = ['config', 'etherius', 'get']
    date_list = ['year', 'month', 'day', 'hour']
    idate = []
    edate = []
    param = []
    # choose config command for cfg
    if command[1] == 'glonass':
        idate_request = ['config', 'glonass', 'get', 'init_date']
        edate_request = ['config', 'glonass', 'get', 'endp_date']
        alma_stage = dict(data_path='alma',
                          data_type='glo_alma',)
    elif command[1] == 'gps':
        idate_request = ['config', 'gps', 'get', 'init_date']
        edate_request = ['config', 'gps', 'get', 'endp_date']
        alma_stage = dict(data_path='alma',
                          data_type='gps_alma',)
    # returninig of init date and end date
    try:
        for item in date_list:
            idate_request.append(item)
            idate.append(shell.config_gs(idate_request))
            edate_request.append(item)
            edate.append(shell.config_gs(edate_request))
            idate_request.pop()
            edate_request.pop()
        # print('Initial date: {0}\nEndpoint date: {1}'.format(idate, edate))
        # retrieving list of parameters
        for item in alma_stage.keys():
            cfg_request.append(item)
            cfg_request.append(alma_stage.get(item))
            param.append(shell.config_gs(cfg_request))
            cfg_request.pop()
            cfg_request.pop()
        param.append(idate)
        param.append(edate)
        return param
    except Exception as e:
        return False
