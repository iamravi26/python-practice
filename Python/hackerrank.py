n=int(input())
if n%2!=0:
    print('Weird')
elif 2<=n<=5:
    print('Not Wierd')
elif n<=20 and n>=6:
    print('Weird')
elif n>20:
    print('Not Weird')


n=int(input())
n=7
for i in range(0,n,1):
    a=i*i
    print(a)

data = dict()
n=5
for i in range(1,n+1,1):
    new=str(i)
    old = str(data.get('name',''))
    data.update({'name':old+new})
print(data['name'])

from codecs import latin_1_decode
from collections import defaultdict
from itertools import count
from re import X

from numpy import append
n=10
m=15

d = defaultdict(list)

d['A']
d['B']

for i in d.items():
    print(i)


name='rraavvuudiinidhd'
data=dict()
for i in name:
    old=data.get(i,0)
    data.update({i:old+1})

print(data)

#count total alphabets(repeted)
#count total alphabets(non-repeted)
#merge all subject names

a=['math','sci','alg','geo','ravi'] 
#q1
l_st=[]
for i in a:
    for k in i:
        l_st.append(k)

print(len(l_st)) 

#q2]
b=set(l_st)       
print(b)
print(len(b))


#q3}
data=dict()
for i in a:
    data.update({'key':data.get('key','')+i}) 

print(data.get('key'))

#q4}which one among the string is repeated

a=['savdjadguhabdajd']
b=a[0]
m=[]
for i in b:
    if b.count(i)!=1:
        m.append(i)
        
        
print(m)
set(m)


#q]

a=['suraj','deepak','uday','abhishek',1,2,3,0.5,1.6,7.8]
l_st=list()
string1=dict()
integer1=dict()
float1=dict()
for i in a:
    if type(i)==str:
      #  old=string1.get('key','')
       # string1.update({'key':old+i})
        # string1.update({i:i})
        
       # l_st.append(i)
       pass
    pass

text ='''In publishing and graphic design, Lorem ipsum 34 is a placeholder text commonly used to demonstrate 
the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used
as a placeholder before final copy is available. It is also 56 used to temporarily replace text in a process called greeking,
which allows designers to consider the form of a webpage or 89 publication, without the meaning of the text influencing the design.

Lorem ipsum is typically a corrupted version of De finibus bonorum 90 et malorum, a 1st-century BC text by the Roman statesman and philosopher Cicero, 
with words altered, added, and removed to make it nonsensical and improper 87 Latin.'''

#index= text.find('1st')
#print(index)

#indexend= text.find('Latin')
#print(indexend)

#text[50:80]
#text[0]
b={'text':text}

for i in text:
    if i.isdigit()==True:
        print(i)
        text1=b.get('text')
        old=text1.replace(i,'')
        b.update({'text':old})
        


#count total char
#count total words
#remove number
#repeat same

def myfunc(n):
  return lambda a : a * n

# def myfunc(n):
#     return n

mydoubler = myfunc(2)

print(mydoubler(11))


#printing matrix
n=input('enter n')
print(n)
m=input('enter m')
print(m)


import numpy
print( numpy.eye(3,3, k = 0))


l = []
dir(zip())
for i in range(10):
    for j in range(10,20):
        if i %2 ==0 and j %2 == 0:
            l.append(i**j)


# Iterable
l = [i**2 for i in range(10) if i %2 ==0]
l = [i**2 for i in range(10) if i %2 ==0]
for i in l:
    print(i)

l = [i**j for i in range(10) for j in range(10,20) if  i %2 ==0 and j %2 == 0]
r = range(10)
for i in r:
    print(i)
#generator
l = (i*j for i in range(1,10) for j in range(1,11))
l.__next__()


# enumerator
r = enumerate(range(10,20))  
for i,j in r:  #i-index  j- value : r could be any sequnce:- list,set,dict,tuple
    print(i,j)


r = map(lambda x:x**2,range(10))
for i in r:
    print(i)

r = filter(lambda x:x%2 == 0,range(10))
dir(r)
for i in r:
    print(i)

r = zip(range(10),range(10))
for i in r:
    print(i)


a = 10
def outer():
    global a
    b = 10
    def inner():
        nonlocal b
        global a
        c =10
        b = 100
        print(b)

def fun():
    aaa = 10

fun()
aaa





#find the runner up score
a=[4,8,9,3,4,6]
a.sort(reverse=False) #acending
print(a[-2])

#by taking multiple input rom the user 
a=list(input().split())
l=list(set(a))
l.sort(reverse=False) 
print(l[-2])   

#q2] sum all the number
num=[1,2,3,4]
sum=0
for i in num:
    sum=sum+i

print(sum)

#Q3]multiply all the number
mul=1
for i in num:
    mul=mul*i
print(mul)

#4]find largest and the smallest
l=[2,45,67,89,4,5,6,89]
a=list(set(l))
a.sort(reverse=False)
print("largest=",a[-1])
print("smallest=",a[0])

#5] Write a Python program to get a list, sorted in increasing order by 
# the last element in each tuple from a given list of non-empty tuples.

a=[(1,2),(3,1),(4,6),(2,3)]
a.sort(key=lambda x:x[1])




#6]Write a Python program to check a list is empty or not

a=[1,2]
print('list is empty')if a==[] else print("list is not empty")

#7]Write a Python function that takes two lists and returns True if they have at least one common member. 

a=[1,2,3,4,5]
b=[6,2,7,8,9,10]
for i in a:
    for k in b:
        if i==k:
            print("true")
            break
        else:
            continue

#8] Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)

#9] 