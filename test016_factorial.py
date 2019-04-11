#factorial

def factorial(x):
    ans = 1
    if x==1:
        print "factorial of 1 is:",x
    elif x != int(x) or x < 0:
        print "Please enter interger no."
    else:
        for i in range(1,x+1,1):
            ans = ans * i
        return ans
print factorial(1)