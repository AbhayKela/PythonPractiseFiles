# local & global variable
cheese='swiss'


def cooking():
    print ("Making dinner");


    
def make_a_pizza():
    cheese='cheddar'
    cooking()
    pizza='a {} pizza'.format(cheese)
    print (pizza);

make_a_pizza()

