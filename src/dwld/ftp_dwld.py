import ftplib
import datetime

def ftp_loader(ftp, data_format, year, month, day):
    filename = 'MCCJ_'
    filename += year[-2:] + month + day + data_format
    # ftp.retrlines('LIST')
    try:
        import os, sys
        main_path = (str(os.path.realpath(os.path.dirname(sys.argv[0])))) + '/out/alma/'
        out_file = open(main_path + filename, 'wb')
        ftp.retrbinary("RETR " + filename, out_file.write)
        print('{0}\tFile {1} downloading complete'.format(datetime.datetime.now(), filename))
        out_file.close()
    except Exception as e:
        print('{0}\tFile {1} loading error: {2}'.format(datetime.datetime.now(),filename, e))
    return ftp    

def ftp_worker(addr = 'ftp.glonass-iac.ru',
               data_format = '.agl',
               path = '/MCC',
               idate = ['2016', '01', '01'],
               edate = ['2016', '01', '02']): 
    try:
        print('{0}\tTrying to connect to {1}'.format(datetime.datetime.now(), addr))
        ftp = ftplib.FTP(addr)
        print('{0}\tConnection to {1} established'.format(datetime.datetime.now(), addr))
        ftp.login()
        ftp.getwelcome()
        print('{0}\tTrying to login'.format(datetime.datetime.now()))
        ftp.cwd(path)
        print('{0}\tRoot path: {1}'.format(datetime.datetime.now(), path))
        # retrieving list of years
        list_of_years = [year for year in range(int(idate[0]), int(edate[0])+1)]
        # for every year in list if years
        for folder in list_of_years:
            print(list_of_years)
            choosen_path = path + '/' + str(folder)
            print('{0}\tChange working directory to: {1}'.format(datetime.datetime.now(), choosen_path))
            ftp.cwd(choosen_path)
            ftp = ftp_loader(ftp, data_format, idate[0], idate[1], idate[2])
        ftp.close()
        return True
    except Exception as e:
        print('{0}\t{1}'.format(datetime.datetime.now(), e))
        print(ftp.close())
        return False



#def retr_files(path, init_date, endpoint_date):
#    cwd_ftp(connect_ftp(), path)