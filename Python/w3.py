#variables 
from re import M


x,y,z= 3  #"ravi",'dekh le' #we can declare variable in a line as well but uday ne bola the it act as tuple(varify)


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x,y+z)
#k=9
#print(z+k)#error dega coz we can add same data types
a = "Hello, World!"
print(a[5])

for x in "banana":
  print(x)

txt = "The best things in life are free!"
print("free" in txt)


a = "The best things in life are free!"
print("The" not in a)
print(a[:11])

b="Ravi gupta"
print(b[-5:-2])

c= "Hello bajhqb World!"
print(c.split())


print(c[-6:-2])
print(c.upper())
print(c.lower())


class MyClass:
  pass

MyClass.__name__
type(MyClass)
isinstance(MyClass,type)
MyClass()

