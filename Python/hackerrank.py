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

from collections import defaultdict
from itertools import count

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
