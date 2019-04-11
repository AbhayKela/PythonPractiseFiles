class Vehicle(object):
    def __init__(self,gas,type1,company):
        self.gas   = gas
        self.type1 = type1
        self.company=company


    def description(self):
        print "My new %s is of %s runs on %s" % (self.type1,self.company,self.gas)


toyota = Vehicle ('gasoline','4 wheeler','Toyota')
honda  = Vehicle ('gasoline','2 wheeler','Honda')

toyota.description()
honda.description()