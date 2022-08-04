
#Q1)

class Account1:
    type="Savings account"
    def __init__(self,account_num,name,balance) -> None:
        if not isinstance(account_num,int):
            raise AttributeError("account_num should be int")
        
        if not isinstance(name,str):
            raise AttributeError("name should be string")

        self._account_num=account_num
        self._name=name
        self._bal=balance

    def addbalance(self,value):
        if isinstance(value,int):
            self._bal+=value
            self.display()

    
            
                
    def withdraw(self,value):
        if value>self._bal:
            print("insufficient balance")
        else:
            self._bal-=value

    def display(self):
        print(self._bal)




        
b=Account1(12345,"Ravi",10000) 
c=Account1(99099,"ravi",2000) 
Account1.type
b._account_num
b._bal
b._name
b.type
b.addbalance(5000)
b.withdraw(2000)
b.withdraw(15000)
c.withdraw(100000)
c._bal
c._name
c.addbalance(800)
c.display()
c._bal=''
