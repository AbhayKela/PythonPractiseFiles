# Make sure that the_flying_circus() returns True
def the_flying_circus():
    print("write any one digit number from 1 to 9\n")
    ans=input()
    ans1=int(ans)
    if 2**ans1==256:    # Start coding here!
        # Don't forget to indent
        # the code inside this block!
        print("Given number is 8")
    elif  2**ans1>9 and 2**ans1<512:
        # Keep going here.
        # You'll want to add the else statement, too!
        print("Given number is greater than 3 but less than 10")
    else:
        print("Return nothing")
(the_flying_circus())