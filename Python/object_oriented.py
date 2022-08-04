#code by Uday
class ABC(object):
    pass

a = ABC() #obejct banaya hai
str(a) 
print(a)
dir(a)
a.__class__

type(a)
ABC.__name__

type(ABC)
isinstance(ABC,type)


class Account:
    Type = "Saving" #class variable
    def __init__(self,Account,Name) -> None:
        if not isinstance(Account,int):
            raise AttributeError('Account should be int')

        self._account = Account #instance variable
        self._name = Name


    @property  #property pe he setter getter lagata hai
    def Account(self): #ye instance lvl pe update karega
        return self._account
    
    @Account.getter
    def Account(self):
        return self._account


    @Account.setter
    def Account(self,value):
        if isinstance(value,int):
            self._account = value
        else:
            raise AttributeError('Account should be int')



    def display(self):
        print(id(self))

    def __repr__(self) -> str:   #if instance represent karega to ye call hoga
        return f"Account(Name : {self.Name}, Account : {self.Account})"

    def __str__(self) -> str:  #print karega to ye call hoga
        return "String format o ACCount class"

    @classmethod #class lvl pe method hota hai 
    def ChangeType(cls,value):#cls likha hai iske class lvl pe hai"self" hai to instance lvl pe hai
        cls.Type = value







dir(Account)
a = Account(12345,"Ravi")

Account.Type
a.Type = 'General'

a.Type = 'General'
Account.ChangeType("ABC")
a.__dict__ 
a._account
a.Account
repr(a)
print(a)
type(a)
str(a)
dir(a)
a.Name  
a.Account
a.display()
id(a)
a.Account = 1000



import math
class Circle:
    
    def __init__(self,radius) -> None:
        self._radius = radius
        self._area = None
        self._parameter= None

    @property  #it will act as getter only,hum radius ka value change nahi karana chahte
    def radius(self):
        print(".............getter")
        return self._radius

    @radius.setter
    def radius(self,value):
        print('setter..............')
        if not isinstance(value,str): #int & float chalega
            self._radius = value
           
        else:
            raise ValueError('Value should be int')

    @property
    def area(self):
        if  not self._area:#if self._area me already us radius ka value hai to vahi show karega
            print('area calculating ............')
            self._area = (math.pi)*pow(self.radius,2)
        return self._area

    @property
    def parameter(self):
        if not self._parameter:#means parameter me value nahi hai
            print("parameter is calculating......")
            self._parameter=2*(math.pi)*self.radius
        return self._parameter
    
c = Circle(10)
c.radius
c.radius = ""
c.radius = 11
c.area
c.parameter

# classmethod , staticmethod

class Class:
    def instance_method(self):
        print('This is instance method')

    @classmethod
    def classmethod(cls):
        print('This is class Method')

    @staticmethod
    def staticmethod():
        print('This is static Method')


c = Class()
dir(c)
c.instance_method()
c.staticmethod()
Class.classmethod()



