#Modules import
import os
from ftplib import FTP

#connecting to FTP
connect = str('ftp.unibe.ch')
ftp = FTP(connect)
print ('Connecting to ', connect , 'FTP')
ftp.login()
print ('Sucess')
directory = str('/aiub/BSWUSER50/ORB/')
print ('BULLET_A.ERP directory :  ' + str(directory))
ftp.cwd(directory)
ftp.retrlines("LIST")

listing = []
ftp.retrlines("LIST", listing.append)
listcount = len(listing)
# i - counter
i = 0
while i<= (listcount - 1):
    file_properties = listing[i].split(None, 8)
    filename = file_properties[-1].lstrip()
    i = i + 1
    if filename == 'BULLET_A.ERP':
        Cel_Mech_GEN_Path = input('input path to your Celestial Mechanics GEN directory (like this:  E:\Celestial Mechanics\GEN\)')
        local_filename = os.path.join(Cel_Mech_GEN_Path, filename)
        lf = open(local_filename, "wb")
        ftp.retrbinary("RETR " + filename, lf.write, 8*1024)
        print('DONE!')
        lf.close()
        break