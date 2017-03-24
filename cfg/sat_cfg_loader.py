def configuration_summary(params)
    ext_dict = dict(init_date  = [],
                    endp_date  = [],
                    data_path  = '',
                    eph_type   = '',
                    bull_type  = '',
                    frc_type   = '',
                    stat_param = '',
                    data_types = '',
                    )
    # initial parameters configuration
    cfg_request = ['config', 'etherius', 'get']
    cfg_alma = ['alma']
    date_list = ['year', 'month', 'day', 'hour']
    dwld_config = []
    idate = []
    edate = []
    param = [command[1]]
    # choose config command for cfg parsing
    if command[1] == 'glonass':
        idate_request = ['config', 'glonass', 'get', 'init_date']
        edate_request = ['config', 'glonass', 'get', 'endp_date']
        glo_alma = '.agl'
        glo_stat = '.glo'
        glo_rinx = '.yyg'
    elif command[1] == 'gps':
        idate_request = ['config', 'gps', 'get', 'init_date']
        edate_request = ['config', 'gps', 'get', 'endp_date']
        gps_alma = '.agp'
        gps_stat = '.gps'
        gps_rinx = '.yyn'
    #returninig of init date and end date
    for item in date_list:
        idate_request.append(item)
        idate.append(config_gs(idate_request))
        edate_request.append(item)
        edate.append(config_gs(edate_request))
        idate_request.pop()
        edate_request.pop()
    print('Initial date: {0}\nEndpoint date: {1}'.format(idate, edate))
    # returning of
    cfg_alma.append(gps_alma)
    for item in ext_dict.keys():
        try:
            cfg_request.append(item)
    # starting of dwld script
    #import ftp_dwld