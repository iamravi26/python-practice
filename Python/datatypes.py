'''
1. String
2. int
3. float
4. list
5. tuple
6. set
7. dict
'''

# String

from ctypes import addressof


s = 'hi how are youHHH'

a='kar lenge tu tension na le'
b="chinta chita saman hai"
c=a+b #'kar lenge tu tension na lechinta chita saman hai'
c=a+'   '+b #'kar lenge tu tension na le   chinta chita saman hai'


s.lower() 
s.capitalize() #Converts the first character to upper case
s.upper()
s.split() #['Hi', 'how', 'are', 'youHHH'] it will split the strungs into substrings
s.startswith('Hi')
s.endswith('you')
s.strip()  #remove spaces from both ends of string
s.count('H')
s.index('o')#it will throw error if not found the element in the string
s.find('o')#Searches the string for a specified value and returns the position of where it was found
#find does not throw error if not find in the string it gives -1 as the output
s.isdigit()
'434'.isdigit()
s.lstrip()
s.replace('Hi','hiiiiiiiiiiii')
s.removeprefix()
s.title() #Converts the first character of each word to upper case 'Hi How Are Youhhh' last me lower kar diya hai
s.__delattr__
s.__dir__()




age = 36
txt = "My name is John, I am " + age #we can add string & int we can do this by using "format()"

quantity = 3
itemnum = 567
price = 49.95
myorder = "I want {0} pieces of item {1} for {2} dollars."
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemnum, price))

txt = "We are the so-called 'Vikings' from the north."#single quootes are allowed in double quotes
#if want to use double quotes in double quotes in double quotes the have to use escape char "\" 
txt = "We are the so-called \"Vikings\" from the north." #this will not throw error 

# int

a = "101"
int(a,base=2)
int(a,base=10)
b = 10
bin(b)
hex(b)
oct(b)
chr(b) #kya hai bhai ye 
chr(122)
ord('z')
float(b)
str(b)
list([b])

# float

c = 17.5645
int(c)
round(c,0)
round(11.59)

round(9.5)
round(8.5)


# list

a = [1,2,3,4,5,4,4]
type(a)
id(a)
id(a[0])
a[0]=20
a[0]
id(a[0])
id(a)


a = {1,2,3,4,5,4,4}
print(a) #a will not take repeated number
type(a)
id(a)
id(a[0])
# a[0]=20#if can not do this then hows the set is mutabe? #can not be done in tuple
a[0]
id(a[0])
id(a)

dir(a)
a.append(5)
a.insert(6,19)
a.remove(19)
a.remove(4) #it will delete the element u enter from the list
a.pop(4) #it will delete the element of the position u enter
a.pop() #it will remove the last item
del a[1]
del a #will delete the complete list

a.count(4)
a.extend([4,5,7]) #it will simply extend the list 
a.append([4,5,7]) #it will add a new list as an one element at the end
a.index(1)
a.reverse()
a.sort(reverse=True) #decending
a.sort(reverse=False) #acending
len(a)

a=10
id(a)
b=20
a = a+b # assign new memory address
id(a)

a += b # assign same memory address
id(a)

l = [{'a':1,'z':9},{'a':15,'z':7},{'a':0,'z':19}]
l.sort(key=lambda x: x['z'])

a=[1,2,3,4,4,5,6,7,8,'a',6,'c','c','d','d']
a[7]= 9







a = (1,2,3)

b = a.copy() # deepcopy gives u two diff adress so if u make changes in a it will not affect b(only for mutables)
id(a),id(b)

c = a # shallow copy
id(a),id(c)
a.append(199)
import copy
from dataclasses import replace


d = copy.deepcopy(a)
id(a),a
id(d),d
d.append(10)

d = copy.copy(a)
id(a),a
id(d),d
d.append(10)

lt = [[1,2],[3,6]]
id(lt),id(lt[0]),id(lt[1])  

lt1 = copy.copy(lt)
id(lt1),id(lt1[0]),id(lt1[1])
lt1 = lt
id(lt1),id(lt1[0]),id(lt1[1])
lt[0].append(84)


lt2 = copy.deepcopy(lt)
id(lt2),id(lt2[0]),id(lt2[1])
lt[1].append(84)


lt.count(1)
a.sort()
sorted(a)



a = [9,5,4,0,3,0,0,1]
# 0,0,0,9,5,4,3,1
# 95431000
for i in range(0,len(a)):
    if a[i] ==0 :
        # value = a.pop(i)
        a.remove(0)
        value = 0
        print(value)
        # a.insert(0,value)
        a.append(value)

# tuple

a = (1,2,3,8,6,7)
id(a)
print(a)
id(a[0])
a[0]=80
a.count(1)
a.index(1)
sorted(a)#tuple me sorted use karana hota hai
a.sort()#this will yrow error

id(a)
b = a

id(b)
a=([1,2,3],[4,6,7])
type(a)
a[0].append(90)


# 

a = input('Enter no : ')
a.split()


l = [int(i) for i in input('Enter no : ').split() if int(i) < 5]


l = []

a = input('Enter no : ')
for i in a.split():
    l.append(int(i))


a=2**3
a+=2
True is 1 

'''Identity operators are used to compare the objects,
 not if they are equal, but if they are actually the same object, with the same memory location'''
 






thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[0:4] = ["blackcurrant", "watermelon",3,4,5]
print(thislist)

a=[1,2,3,3]
a.insert(2,'R')
b={6,7,7,7,7,7}
a.extend(b)



#Slicing


a = range(0,100,2)

b = range(100)
a = list(b)
# start : end-1: increament
a[9]
a[-1:-10:-2]

a[::-1]

a[1:10:2]

a[:10]
a[15:20]
s = 'dsdgdfgdfg'
s[-1]
s[:5:-1]

a[50:10:-1]

c = (1,2,3,4,5)
c[::-1]

s = {1,2,3,4}
s[0]

s = {1:1}
s[0]


# Map
a = list(range(10))

def fun(x):
    return x**2
list(map(fun,a))

#  map(function,iteration)
list(map(lambda x:x**2,range(1,100,5)))

list(map(lambda x:float(x),range(100)))
list(map(float,range(100)))

l1=[1,2,3,4,5]
list(filter(lambda x:x%2==0,l1))
l2=[1,2,3,4,5]


list(map(lambda x,y:x+y,l1,l2))



# filter
# filter(function,sequance)
list(filter(lambda x: x != 0 and x%2==0,set(range(100))))


# Zip(sequence,sequence)

a = range(10)
b = range(100)
origin = (3,9)


(0,0),(1,1)
l = list(zip(a,b))

m=list(map(lambda x: origin[0]*x[0]+origin[1]*x[1],l))
list(filter(lambda x:x < 50,m))

list(filter(lambda x:x < 50,map(lambda x:origin[0]*x[0]+origin[1]*x[1],zip(a,b))))

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)

newlist = ['hello' for x in fruits]

list2=[x.upper() if x!="banana"else 'Ravi' for x in fruits]

a=[1,2,3,8,4,5,6]
c=a.copy()
print(c)
a.sort()
a.sort(reverse=True)
a.reverse()

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3,4]
#way1
list3=list1+list2

#way2
for x in list2:
    list1.append(x)
print(list1)

#way3
a=[list1.append(x) for x in list2 ]  #ask suraj how to use list comprehensions

#way4
list1.extend(list2) 
print(list1)


a=(1,2,3,4,5,6)
b=list(a)
b[1]=10
print(b)
a=tuple(b)
print(a)


a={'a':{'k':1,'b':2,'c':3},'b':{'x':1,'y':2,'z':3},'c':{'x':1,'y':2,'z':3}}
a={'a':1,"b":2,"c":3}
b=a #if u do this whatever chnges u made in a will be visible b to avoid that use copy()
a['a']=10
print(b)#changes b me bhi hua

c=a.copy()#here c is at diff adress
a['a']=10
print(c)#there will be no changes c coz of changes done in a like previous example


print(a['c'])
a.get('a')
b=a.keys()
c=a.values()
a.items()
a['d']=4
print(a)
a['a']=3
if 'a' in a:
    print(True)


del a['c']
a.pop('a')

for x in a:
    print(a[x]);print(x)
    

for x in a.values():
    print(x)


for x in a.items():
    print(x)

l1=[1,2,3,]
l2=[10,20,30,40,50]
l3='python'

list(zip(l1,l2,l3))

l=[2,3,4]
a=[]
for x in l:
    a.append(x**2)

print(a)   #output [4, 9, 16]

[x**2 for x in l]  #output [4, 9, 16]


l1=[1,2,3,4,5]
l2=[11,22,33,44,55]
a=list(zip(l1,l2))
c=[x+y for x,y in a] #output [12, 24, 36, 48, 60]

#or
list(map(lambda x,y:x+y,l1,l2)) #[12, 24, 36, 48, 60]

l=[1,2,3,4]
[x for x in l if x%2==0]

a=range(10)
list(filter(lambda x:x<25,map(lambda y:y**2,a)))
#alternative
[x**2 for x in a if x**2<25]


x=input("enter the username")
print('user name is:'+x)


d={'p':1,'y':2,'t':3,'h':4}
a,*b=d
print(a)
print(*b)
d1={'p':1,'y':2}
d2={'t':3,'h':4}
d3={'h':5,'o':6,'n':7}
d={**d1,**d2,**d3}
type(d)