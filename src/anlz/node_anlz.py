import sys, os, shutil, time

path_to_out_files = input('Enter path to *.OUT files (like this E:\OUT):')
files = os.listdir(path_to_out_files);
amount_of_out_files = len(files)
path_to_txt_files = input('Enter path, where i should save a file with eccentricity data (like this E:\Elements):')

number = input('Enter number of Satellite (1-24 for GPS)')

if int(number) < 10:
    sat_number = '10'+number
else:
    sat_number = '1' + number

def node_read(out_file, sat_number):
        out = open(out_file, 'r')
        count = 0
        number_of_sat_string = 0
        node_linelist = []
        # parsim stro4ku s nomerom sputnika
        for line in out.readlines():
            node_linelist.append(line)
            try:
                if line[11]+line[12]+line[13] == sat_number:
                    number_of_sat_string = count
                else:
                    count = count + 1
            except:
                count = count + 1
        #vydelyaem node
        node_string = 0
        node = ['None', 'None', 'None', 'None']
        try:
           while node[3] != 'NODE':
                node_line = node_linelist[number_of_sat_string+node_string]
                node_string = node_string + 1
                node = node_line.split(' ')
                if len(node) < 4:
                    node = ['None', 'None', 'None', 'None']
                print(node)
           out.close()
           return(node[11])
        except:
            # esli fail *.out ispor4en
            out.close()
            return('0')



node = []
counter = 0
while counter != amount_of_out_files:
    out_file = str(path_to_out_files) + '\ '[:-1] + files[counter]
    print(out_file)
    node.append(node_read(out_file, sat_number))
    print(counter)
    counter = counter + 1

node_txt = open(path_to_txt_files + '\ '[:-1] + 'node' + sat_number +'.txt', 'w')
for value in node:
    node_txt.write(value + '\n')
    print(value)
print('Done!')
node_txt.close()