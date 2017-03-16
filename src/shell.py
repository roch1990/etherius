import sys, os

def command_validation(command, arg_num):
    """Command validation function"""
    if command == 'config' and arg_num != 5:
        print('Command argument error')
        print('You entered', arg_num, 'arguments. Expected 4')
        return False
    else:
        return True

def config_gs(*command):
    import eth_cfg_loader
    if command_validation(command[0][0], len(command[0])):
        param = command[0][1]
        method = command[0][2]
        stage = command[0][3]
        key = command[0][4]
        print(eth_cfg_loader.get_inf(param, stage, key))
        return True
    else:
        return False

command = ['']

while command[0] != 'exit':
    """
    prefix| type   |  method | key | value
    ______|________|_________|_____|______
    config|etherius| get     |stage| key
          |glonass | set     |  
          |gps     |
    """
    command = input().split(' ')
    if command[0] == 'config':
        config_gs(command)
else:
    print('Thank you for using this programm!')
    input('Press Enter to quit')
    sys.exit