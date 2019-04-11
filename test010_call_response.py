def square(n):
    squared = n ** 2
    print("%f squared is %f " % (n, squared))
    return squared


square(10)
square(3.55666654)


#######################################################

def power(base, exponent):
    ans1 = base ** exponent
    print("%f powered %f is %f" % (base, exponent, ans1))
    return ans1


power(37, 4)
power(4, 37)


#####################################################

def func1(n):
    n = n ** n
    return n


def func2(m):
    return func1(m) + (m * m)


print(func1(2))
print(func2(3))


########## Function calling function #########################
def cube(number):
    return number * number * number


def by_three(number):
    if cube(number) % 3 == 0:
        return cube(number)
    else:
        return False


print(cube(2))
print(by_three(3))
