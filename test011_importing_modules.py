from math import sqrt

print(sqrt(25))
"===================================================="
########### Check maths directory ################
"""import math
everything=dir(math)
print everything
print math.pi"""
####################################

def biggest_number(*args):
    print(max(args))
    return max(args)


def smallest_number(*args):
    print(min(args))
    return min(args)


def distance_from_zero(args):
    print(abs(args))
    return abs(args)


biggest_number(-10, 10000, 0.0005, 1)
smallest_number(-10, 10000, 0.0005, 1)
distance_from_zero(-0.000000080)
printP +1 248.614.2400 ext 1298 | C +1 248.251.6134.
"==============================================================="


###########################################################

def distance_from_zero(x):
    if type(x) == int or type(x) == float:
        print(abs(x))
        return abs(x)
    else:
        print("Nope")
        return "Nope"

distance_from_zero(3.45)
