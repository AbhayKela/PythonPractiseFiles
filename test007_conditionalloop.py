# script for conditional looping 

def cars():
    print("please select car category from the following")
    print("onroad or offroad?")
    answer = input().lower()
    if answer == "onroad" or answer == "on":
        print("Its really nice")
    elif answer == "offroad" or answer == "off":
        print("Its a bad ass")
    else:
        print("no option provided or wrong option provided")
cars()

# part II

#def powertrain_1():
#   if 2**3==8:
#        return "automcatic transmission"
#def powertrain_2():
#    if 2**3!=7:
#        return"manual transmission"

#print (powertrain_1())
#print (powertrain_2())*/