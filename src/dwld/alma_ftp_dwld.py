try:
    import ftplib
    import datetime
    import calendar
    import os
    import sys
except ImportError as e:
    print("{0}\t{1}".format(datetime.datetime.now(), e))


def ftp_loader(ftp, data_format, year, month, day):
    filename = 'MCCJ_'
    try:
        filename += str(year)[-2:] + \
                    ("%02d" % month) + \
                    ("%02d" % day) + \
                    data_format
    except TypeError as e:
        print("{0}\t{1}".format(datetime.datetime.now(), e))
    # ftp.retrlines('LIST')
    try:
        # parameters initialaizing
        sat_path = ''
        # format cheking
        if data_format == '.agl':
            sat_path = 'glo/'
        if data_format == '.agp':
            sat_path = 'gps/'
        # output data file shaping
        main_path = (str(os.path.realpath(os.path.dirname(sys.argv[0])))) + '/out/alma/' + sat_path
        out_file = open(main_path + filename, 'wb')
        # retrieving of data file from ftp server
        ftp.retrbinary("RETR " + filename, out_file.write)
        # print('{0}\tFile {1} downloading complete'.format(datetime.datetime.now(), filename))
        out_file.close()
    except Exception as e:
        print('{0}\t{1}: {2}'.format(datetime.datetime.now(), filename, e))
        print('{0}\tContinuing . . . '.format(datetime.datetime.now()))
    return ftp


def ftp_worker(addr='ftp.glonass-iac.ru',
               data_format='.agl',
               path='/MCC',
               idate=['2016', '01', '01'],
               edate=['2016', '01', '02']):
    # print(data_format)
    # tryng to establishing connection
    try:
        print('{0}\tTrying to connect to {1}'.format(datetime.datetime.now(), addr))
        ftp = ftplib.FTP(addr)
        print('{0}\tConnection to {1} established'.format(datetime.datetime.now(), addr))
        ftp.login()
        ftp.getwelcome()
        print('{0}\tTrying to login'.format(datetime.datetime.now()))
        ftp.cwd(path)
        print('{0}\tRoot path: {1}'.format(datetime.datetime.now(), path))
        # retrieving init date and endp date in datetime format
        init_date = datetime.date(int(idate[0]),
                                  int(idate[1]),
                                  int(idate[2]),
                                  )
        endp_date = datetime.date(int(edate[0]),
                                  int(edate[1]),
                                  int(edate[2]),
                                  )
        # for every year in list if years
        print('{0}\tStart downloading'.format(datetime.datetime.now()))
        print('{0}\tPlease wait'.format(datetime.datetime.now()))
        # day increment
        while init_date <= endp_date:
            year = init_date.year
            choosen_path = path + '/' + str(year)
            # print('{0}\tChange working directory to: {1}'.format(datetime.datetime.now(), choosen_path))
            ftp.cwd(choosen_path)
            ftp = ftp_loader(ftp,
                             data_format,
                             init_date.year,
                             init_date.month,
                             init_date.day,
                             )
            init_date += datetime.timedelta(days=1)
        print('{0}\tDownload complete'.format(datetime.datetime.now()))
        ftp.close()
        print('{0}\tConnection to {1} closed'.format(datetime.datetime.now(), addr))
        return True
    except Exception as e:
        print('{0}\t{1}'.format(datetime.datetime.now(), e))
        ftp.close()
        print('{0}\tConnection to {1} closed'.format(datetime.datetime.now(), addr))
        return False
