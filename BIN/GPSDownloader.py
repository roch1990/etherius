#-------------------------------------------------------------------------------
# Name:        Gps Ephemeris Stealer
# Purpose:
#
# Author:      Eugene Gildin
#
# Created:     01.11.2013
# Copyright:   (c) User 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Modules import
from ftplib import FTP
import os, zipfile

# Select Directory

userdir = input('Write directory here (Example:   C:\Documents\) ->')
cwd = os.chdir(userdir)
print('Choosen directory -', os.getcwd())

# Creating of new directory for eph

print('Creating of new folder in your directory, named - GPS Ephemeris')
try:
    os.mkdir('GPS Ephemeris')
    print('Creating complete!')
except:
    print('WARNING! This folder is already exist!')
downdir = os.chdir(os.getcwd() + ('\GPS Ephemeris'))

# Connect to GLONASS FTP

connect = str('igscb.jpl.nasa.gov')
ftp = FTP(connect)
print ('Connecting to ', connect , 'FTP')
ftp.login()

# Changing directory at server

directory = str('/pub/gps/')
print ('GPS Ephemeris directory :  ' + str(directory))
ftp.cwd(directory)

# Calculating of Julian Date (Michael Soffel, Ralf Langhans - Space/Time Reference Systems 2013)

def Julian_date(greg_date):
    list = greg_date.split('.')
    if int(list[1]) <= 2 :
        list [2] = int(list[2]) - 1
        list[1] = int(list[1]) + 12
    A = int(int(list[2])/100)
    B = 2 - A + int(A/4)
    JD = int(365.25 * (int(list[2]) + 4716)) + int(30.6001 * (int(list[1]) + 1)) + int(list[0]) + B - 1524.5
    return(JD)

# Calculating of GPS-week (http://astro.tsu.ru/TGP/text/2_6.htm)

def Week_Number(Julian_day):
    return(int((Julian_day-2444244.5)/7))

# Input and calculating of firts GPS-week

begin_date_input = str(input('Input first date dd.mm.yyyy'))
First_week = Week_Number(Julian_date(begin_date_input))
print(First_week)

# Input and calculating of second GPS-week

end_date_input = str(input('Input second date dd.mm.yyyy'))
Second_week = Week_Number(Julian_date(end_date_input))
print(Second_week)

# Downloading

print('Downloading')
while First_week <= Second_week :
    if First_week < 1000 :
        str_First_week = '0' + str(First_week)
    else :
        str_First_week = str(First_week)
    eph_directory = directory + '/' + str_First_week + '/'
    ftp.cwd(eph_directory)

    ftplist_eph = []
    ftp.dir(ftplist_eph.append)

    for line in ftplist_eph:
        print('.', end=' ')
        ephfname = ''.join(line.split()[8])
        if ephfname[-6:-2]=='.sp3' :
            cfname = ''.join(str(First_week))
            local_filename = os.path.join(str(cfname+ephfname))
            lf = open(local_filename, "wb")
            ftp.retrbinary("RETR " + ephfname, lf.write, 8*1024)
            lf.close()

    First_week = First_week + 1

print('Downloaded Succesfully! ')

# Closing FTP connection
ftp.quit()





