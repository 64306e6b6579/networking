"""
Asks enter a subnet mask in 255.255.255.0 or 255.255.224.0 and
it converts to /something
"""

# first take an input of subnet mask make a list out of it and convert to integers

subnet = input('enter a subnet: ').split('.')


def check_subnet_class():
    subnetmask = [eval(i) for i in subnet]
    if -1 < subnetmask[0] < 127:
        return 'it is A class'
    elif 127 < subnetmask[0] < 192:
        return 'it is B class'
    elif 191 < subnetmask[0] < 224:
        return 'it is C class'
    elif 223 < subnetmask[0] < 240:
        return 'it is D class'
    elif 239 < subnetmask[0] < 255:
        return 'it is E class'
    else:
        return 'incorrect Entry'


print(check_subnet_class())
