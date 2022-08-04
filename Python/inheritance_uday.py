class Parent:
    def __init__(self,name) -> None:
        self.name = name
        self.car = "BMW"

    def hasbalance(self):
        return 1000000
    
    def hascar(self):
        return "BMW"

    def __repr__(self) -> str:
        return f"Parent(name : {self.name})"
    
class Child(Parent):
    def __init__(self,name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Child(name : {self.name})"



p = Parent("ABC")
p.hasbalance()
p.hascar()

c = Child("Ravi")
c.name
c.hasbalance()
c.hascar()



class Father:
    def __init__(self,name) -> None:
        self.name = name

    def hasbalance(self):
        return 1000000
    
    def hascar(self):
        return "BMW"

    def __repr__(self) -> str:
        return f"Father(name : {self.name})"



class Mother:
    def __init__(self,name) -> None:
        self.name = name

    def hasgold(self):
        return "10kg"
    
    def hashome(self):
        return "10 bhk"

    # def hasbalance(self):
    #     return 100

    def __repr__(self) -> str:
        return f"Mother(name : {self.name})"


class Child(Mother,Father):
    def __init__(self,name) -> None:
        self.name = name

    def hasbalance(self):
        return super().hasbalance()

    def __repr__(self) -> str:
        return f"Child(name : {self.name})"



p = Father("ABC")
p.hasbalance()
p.hascar()

m = Mother('NBM')
m.hasgold()
m.hashome()



c = Child("Ravi")
c.name
c.hasbalance()
c.hascar()
c.hasgold()
c.hashome()

issubclass(Child,Parent)







    
    
