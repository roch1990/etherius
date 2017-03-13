import sys, os, shutil, time

path_to_inp = (str(os.path.realpath(os.path.dirname(sys.argv[0]))) + '\INP\SATORB.INP')
path_to_cel_mech = input('Enter path to Celestial Mechanics! (like this: E:\Celestial Mechanics):')
INP_file = path_to_cel_mech + '\BIN\SATORB.INP'
shutil.copy(path_to_inp, INP_file)

path_to_SP3_files = input('Enter path to sp3 files (like this E:\Ephemerises):')
files = os.listdir(path_to_SP3_files);
#print(files)
number_of_non_pre_files = len(files)
counter = 0
precise_eph = []
while counter != number_of_non_pre_files -1:
    #print(files[counter][-3:])
    if files[counter][-3:] == 'pre':

        precise_eph.append(files[counter])
    counter = counter + 1
print(precise_eph)
number_of_files = len(precise_eph)
print('Total - ' + str(number_of_files) + ' precise ephemerises')

counter = 1

def ReplaceLineInFile(fileName, sourceText, replaceText):
    file = open(fileName, 'r') #Opens the file in read-mode
    text = file.read() #Reads the file and assigns the value to a variable
    file.close() #Closes the file (read session)
    file = open(fileName, 'w') #Opens the file again, this time in write-mode
    file.write(text.replace(sourceText, replaceText)) #replaces all instances of our keyword
    # and writes the whole output when done, wiping over the old contents of the file
    file.close() #Closes the file (write session)

def Zero_append(count):
    if len(count) == 1:
        count = '0000' + count
    elif len(count) == 2:
        count = '000' + count
    elif len(count) == 3:
        count = '00' + count
    elif len(count) == 4:
        count = '00' + count
    elif len(count) == 5:
        count = '0' + count
    else:
        count = count
    return(count)


sleep_time = input('Enter delay between computations (choose time of 1 ephemeris computation at your PC - optimal about 10 sec for i5)')

shutil.copy(str(path_to_SP3_files) + '\ '[:-1] + str(precise_eph[0]), str(path_to_cel_mech) + '\LEOKIN\ORB\ '[:-1] + str(precise_eph[0]))
ReplaceLineInFile(INP_file, 'ENVIRONMENT 1  "CM" "E:\Celestial Mechanics"', 'ENVIRONMENT 1  "CM" "' + str(path_to_cel_mech) + '"')
ReplaceLineInFile(INP_file, 'PREFIL 1  "${CM}\LEOKIN\ORB\STA17212.PRE"', 'PREFIL 1  "${CM}\LEOKIN\ORB\ '[:-1] + (str(precise_eph[0])).upper() + '"')
ReplaceLineInFile(INP_file, '# STA17212', '# ' + (str(precise_eph[0])).upper())
os.startfile(path_to_cel_mech  + r'\BIN\ '[:-1] + 'SATORB.INP')
time.sleep(float(sleep_time))
shutil.copy(str(path_to_cel_mech) + '\SATORB\OUT\SATORB.OUT', str(path_to_cel_mech) + '\SATORB\OUT\SATORB00001.OUT')
time.sleep(float(5))
print(str(precise_eph[0]) + ' ephemeris computation - Done')

while counter != (number_of_files):
    shutil.copy(str(path_to_SP3_files) + '\ '[:-1] + str(precise_eph[counter]), str(path_to_cel_mech) + '\LEOKIN\ORB\ '[:-1] + str(precise_eph[counter]))
    ReplaceLineInFile(INP_file, 'PREFIL 1  "${CM}\LEOKIN\ORB\ '[:-1] + (str(precise_eph[counter - 1])).upper() + '"', 'PREFIL 1  "${CM}\LEOKIN\ORB\ '[:-1] + (str(precise_eph[counter])).upper() + '"')
    ReplaceLineInFile(INP_file, '# ' + str(precise_eph[counter - 1].upper()), '# ' + (str(precise_eph[counter])).upper())
    os.startfile(path_to_cel_mech  + r'\BIN\ '[:-1] + 'SATORB.INP')
    time.sleep(float(sleep_time))
    shutil.copy(str(path_to_cel_mech) + '\SATORB\OUT\SATORB.OUT', str(path_to_cel_mech) + '\SATORB\OUT\SATORB' + Zero_append(str(counter+1)) + '.OUT')
    time.sleep(float(5))
    print(str(precise_eph[counter + 1]) + ' ephemeris computation - Done')
    counter = counter + 1
else:
    print('All went well, computations done')

