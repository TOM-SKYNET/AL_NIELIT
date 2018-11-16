
import abc
class vehicle:
    __metaclass__ = abc.ABCMeta    
    def __init__(self,nameofowner,vehno,noofwheels,presentvalue,yearofmake):
        self.nameofowner = nameofowner
        self.vehno = vehno
        self.noofwheels = noofwheels
        self.presentvalue = presentvalue
        self.yearofmake = yearofmake
        self.buyingprice = 0
    @abc.abstractmethod
    def disp(self):
        pass
        
class car(vehicle):
    def calcDepriciation(self):
        self.buyingprice = self.presentvalue -  5000
    def disp(self):
        self.calcDepriciation()
        print "Owner Name :%s, No :%s, No of Wheels:%d, Present Value:%f, Year %d, Buying Prices:%f"%(self.nameofowner,self.vehno,self.noofwheels,self.presentvalue,self.yearofmake,self.buyingprice)
        
class bus(vehicle):
    def calcDepriciation(self):
        self.buyingprice = self.presentvalue -  10000
    def disp(self):
        self.calcDepriciation()
        print "Owner Name :%s, No :%s, No of Wheels:%d, Present Value:%f, Year %d, Buying Prices:%f"%(self.nameofowner,self.vehno,self.noofwheels,self.presentvalue,self.yearofmake,self.buyingprice)        
class truck(vehicle):
    def calcDepriciation(self):
        self.buyingprice = self.presentvalue -  12000 
    def disp(self):
        self.calcDepriciation()
        print "Owner Name :%s, No :%s, No of Wheels:%d, Present Value:%f, Year %d, Buying Prices:%f"%(self.nameofowner,self.vehno,self.noofwheels,self.presentvalue,self.yearofmake,self.buyingprice)

car = car("ABC","KL12-2333",4,150000,2017)
car.disp()
bus = bus("CDE","KL11-2333",4,5000000,2016)
bus.disp()
