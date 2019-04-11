# write a function to compute volume of sphere with given radius


def vol(rad):
    import math
    pi = math.pi
    volume = ((4/3)*pi*(rad**3))
    print('\n')
    print('1. Volume of sphere: ', volume)
    print('\n')
vol(4)

# To check whether given number is in specified range


def ran_check(num, low, high):
    if num in range(low, high+1):
        print('2.To check if given number is in specified range: %s is not in specified range' % str(num))
    else:
        print('2.To check if given number is in specified range: %s is not in specified range' % str(num))
    print('\n')
ran_check(54, 55, 66)

# To check if number is in range (return boolean)


def ran_bool(num, low, high):
    print('3. Using return boolean check if number is in given range:')
    return num in range(low, high+1)
print(ran_bool(54, 55, 66))
print('\n')

# To write a function accepting in input in string and giving number of upper and lower case characters


def up_low(s):
    d = {'upper': 0, 'lower': 0}
    for c in s:
        if c.isupper():
            d['upper'] += 1
        elif c.islower():
            d['lower'] +=1
        else:
            pass
    print('4. Function for accepting input as string and outputting upper and lower case characters: ')
    print('Original string: ', s)
    print('Number of upper case characters: ', d['upper'])
    print('Number of lower case characters: ', d['lower'])
    print('\n')
s = 'Hi,Abhay how are you doing this weekend?'
up_low(s)

# Return unique list


def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
            x.sort()
    print('5.Function for return of unique list: ', x)
    print('\n')
unique_list([11, 1, 1, 1, 1, 1, 1, 1, 1, 12, 2, 2, 2, 3, 3, 3, 3])

# Multiply


def multiply(numbers):
    result = 1
    for number in numbers:
        result = result * number
    print('6. Multiplying all the number in given list: ',numbers)
    print('Result is:',result)
    print('\n')
multiply([1, 2, 3, -4])

# Check if the a given word is palindrome (ex. helleh, madam etc)


def palindrome(s):
    s.replace(' ','')
    print('7.Function to check Palindrome (string == reverse string): ', s)
    print('Result is', s == s[::-1])
    print('\n')
palindrome('abhay')


# check whether the given string is Pangrams
# steps: Import string, define function, def set with string.ascii (for all the alphabets),
# Convert all alphabet in given sting in lower case, compare both


import string


def ispangram(string1, alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(string1.lower())
print('8.Function to check Pangram (if containing all the alphabets in given string): ')
print('Result is', ispangram('The quick brown fox jumps over the lazy dog'))

print('========= End of Homework =========')