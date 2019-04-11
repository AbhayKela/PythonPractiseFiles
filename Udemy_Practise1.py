name = 'This is global name'

def name1():
    global name
    print ("NAME: ",name)
    def name2():
        name = 'Abhay'
        print ('Hello ',name)
    name2()
name1()
