#-------------------------------------------------------------------------------
# Name:        GLONASS Ephemeride Stealer(GNS) ;)
# Purpose:     You can download GLONASS ephemeris from ftp.glonass-iac.ru by
#              using this small script
# Author:      Eugene Gildin
#
# Created:     31.10.2013
# Copyright:   (c) Eugene 2013
# Licence:     <in that place should be my license>
#-------------------------------------------------------------------------------
# Modules import
from ftplib import FTP
import datetime, os

# Select Directory

userdir = input('Write directory here (Example:   C:\Documents\) ->')
cwd = os.chdir(userdir)
print('Choosen directory -', os.getcwd())

# Creating of new directory for eph

print('Creating of new directory in your folder named - Ephemeris')
try:
    os.mkdir('GLONASS Ephemeris')
    print('Creating complete!')
except:
    print('WARNING! This folder is already exist!')
downdir = os.chdir(os.getcwd() + ('\GLONASS Ephemeris'))

# Connect to GLONASS FTP

connect = str('ftp.glonass-iac.ru') #str(input('Write ftp here (Example:   ftp.glonass-iac.ru) ->'))
ftp = FTP(connect)
print ('Connecting to ', connect , 'FTP')
ftp.login()

# Changing directory at server

directory = str('/MCC/PRODUCTS/')   #str(input('Choose a directory with ephemerides at ftp server (Example: /MCC/PRODUCTS/) ->'))
print ('Ephemerides directory :  ' + str(directory))
ftp.cwd(directory)

# You can choose ephemeris version, of course

eph_type = str(input('What type of eph you want? (Final, Rapid and other)  p.s: beware, only latest measurments have Rapid and Ultra eph  ->'))
lower_eph_type = eph_type.lower()

# Calculating of days number between year start and inputed date

def number_of_days(date):
    global int_number
    date_time = date.split('.')
    year = str(date_time[2])
    full_date = datetime.datetime.strptime(date, '%d.%m.%Y')
    start_year =  str('01.' + '01.' + year)
    start_year_datetime = datetime.datetime.strptime(start_year, '%d.%m.%Y')
    number = str(full_date - start_year_datetime)
    int_number = int(number.split() [0])
    #print(number)
    return()

# Calculating of years numbers between two inputed dates

def number_of_years(first, second):
    global year1, year2, years
    date_time1 = first.split('.')
    year1 = int(date_time1[2])
    date_time2 = second.split('.')
    year2 = int(date_time2[2])
    years = year2-year1
    #print(years)
    return()

#Creating of folder name (first year)

first_list = []
def foldernames(name_day, year_name) :
    global first_list
    find_year_in_year_name = year_name.split('.')
    take_year_after_splitting = find_year_in_year_name[2]
    i = take_year_after_splitting[2:4]
    j = int(name_day)

    while j <=365 :
        if j < 10:
            str_name_day = ('0'+'0'+str(j))
        elif j >= 10 and j <100 :
            str_name_day = ('0' + str(j))
        else :
            str_name_day = j
        foldername = str(i) + str(str_name_day)
        j = j+1
        first_list.append(foldername)
        #print(foldername)
    return()

#Creating of folder name (last year)

second_list = []
def foldernames2(name_day2, year_name2) :
    global second_list
    find_year_in_year_name = year_name2.split('.')
    take_year_after_splitting = find_year_in_year_name[2]
    i = take_year_after_splitting[2:4]
    j = 1

    while j <= name_day2 :
        if j < 10:
            str_name_day = ('0'+'0'+str(j))
        elif j >= 10 and j <100 :
            str_name_day = ('0' + str(j))
        else :
            str_name_day = j
        foldername2 = str(i) + str(str_name_day)
        j = j+1
        second_list.append(foldername2)
        #print(foldername2)
    return()

# Creating of folders name (middle)

middle_list = []
def foldernames3(first_year, second_year):
    global middle_list
    # Indian code, where we looking for two last digits of first year
    find_year_in_year_name1 = first_year.split('.')
    take_year_after_splitting1 = find_year_in_year_name1[2]
    two_last_digits_of_year1 = take_year_after_splitting1[2:4]
    i = int(two_last_digits_of_year1) + 1
    # MORE INDIAN CODE( in this case for second year)
    find_year_in_year_name2 = second_year.split('.')
    take_year_after_splitting2 = find_year_in_year_name2[2]
    two_last_digits_of_year2 = take_year_after_splitting2[2:4]
    j = int(two_last_digits_of_year2) - 1
    daynumber = 1
    # Creating of list
    while i <= j :
        while daynumber <= 365 :
            if daynumber < 10:
                str_daynumber = ('0'+'0'+str(daynumber))
            elif daynumber >= 10 and daynumber <100 :
                str_daynumber = ('0' + str(daynumber))
            else :
                str_daynumber = daynumber

            if i < 10:
                str_i = '0' + str(i)
            else:
                str_i = str(i)
            foldername3 = str_i + str(str_daynumber)
            daynumber = daynumber + 1
            middle_list.append(foldername3)
        daynumber = 1
        i = i + 1
    return()

# Input first date and some nice calculating
begin_date_input = input('Input begining date please (dd.mm.yyyy) :')
number_of_days(begin_date_input)
foldernames(int_number, begin_date_input)

# Input second date and more some nice calculating
end_date_input = input('Input ending date please (dd.mm.yyyy) :')
number_of_days(end_date_input)
foldernames2(int_number, end_date_input)

# Call to function, that calculate difference between first year and second year (I don't know, what it is doing here now :)
number_of_years(begin_date_input, end_date_input)

# Middle years foldername calculating
foldernames3(begin_date_input,end_date_input)

# Full list of folders, ranging by date
if year1 !=year2 :
    list_of_folders = first_list + middle_list + second_list
elif year2-year1 == 1:
    list_of_folders = first_list + second_list
else:
    list_of_folders = list(set(first_list).intersection( set(second_list) ))


# Downloading

print('Downloading')
N = len(list_of_folders)
i = 0
while i < N :
    eph_dir_name = str(list_of_folders[i])
    ndirectory1 = str(directory + eph_dir_name + '/'+ eph_type)
    ndirectory2 = str(directory + eph_dir_name + '/'+ lower_eph_type)
    print('.', end=' ')
    try :
        ftp.cwd(ndirectory1)
    except :
        ftp.cwd(ndirectory2)
    ftplist_eph = []
    ftp.dir(ftplist_eph.append)
    for line in ftplist_eph:
        ephfname = ''.join(line.split()[8])
        if ephfname[-4:-1]=='.gl' :
            cfname = ''.join('.pre')
            local_filename = os.path.join(str(ephfname[:-8] + '.pre'))
            lf = open(local_filename, "wb")
            ftp.retrbinary("RETR " + ephfname, lf.write, 8*1024)
            lf.close()
    i = i + 1

print('Downloaded Succesfully! ')

# Closing FTP connection
ftp.quit()