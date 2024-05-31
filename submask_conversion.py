"""
Asks enter a subnet mask in 255.255.255.0 or 255.255.224.0, and
it converts to /something
"""

# first take an input of ip make a list out of it and convert to integers

###ip1 = input('enter a subnet: ').split('.')

# function that turns the list objects to integers then runs a check and
# to what class this ip belongs


def check_subnet_class(s):
    ip = [int(item) for item in s]
    if -1 < ip[0] < 127:
        return 'it is A class'
    elif 127 < ip[0] < 192:
        return 'it is B class'
    elif 191 < ip[0] < 224:
        return 'it is C class'
    elif 223 < ip[0] < 240:
        return 'it is D class'
    elif 239 < ip[0] < 255:
        return 'it is E class'
    else:
        return 'incorrect Entry'


# function that takes and subnet dotted notation and returns CIDR slash notation

def convert_to_slash_notation(s):
    subnetmask = [int(item) for item in s]
    subnetmask = [bin(item) for item in subnetmask]
    subnetmask = [s[2:] for s in subnetmask]
    count_ones = 0
    for i in subnetmask:
        i.split()
        for b in i:
            if b == '1':
                count_ones += 1
            else:
                pass
    subnet_slash_notation = f'This subnet mask is /{count_ones} bits'
    return subnet_slash_notation


def check_ip_input():
    ip = input('IP: ').split('.')
    for item in ip:
        if item.isnumeric():
            pass
        else:
            print('invalid entry,please us example 10.10.10.10')
            break

