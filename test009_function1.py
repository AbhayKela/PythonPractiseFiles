"""
def tax(bill):
    bill*=1.08
    print "With tax: %f" % bill
def tip(bill):
    bill*=1.15
    print "With tip: %f" % bill

meal_cost=100
meal_with_tax=tax(meal_cost)
meal_with_tip=tip(meal_cost)
"""


def tax(bill) :
    bill *= 1.08
    print("with tax: %f" % bill)
    return bill


def tip(bill):
    bill *= 1.15
    print("with tip: %f" % bill)
    return bill


ans = input("Input the amount of bill\n")
ans1 = int(ans)
tax(ans1)
tip(ans1)
