from tkinter.tix import Tree


def process(s):
    print(id(s))
    s = s + ' world'
    print(id(s))
    return s

var = "Hello"

id(process(var))

id(var)

################

def process(s):
    print(id(s))
    s = s + ' world'
    print(id(s))
    return s

s = "Hello"

id(process(s))

id(s)
################
def process(s):
    print(id(s))
    s.append(6)
    a = 1000
    print(id(s))
    return s

var = [1,2,3]

id(process(var))

id(var)





################
def process(s):
    print(id(s))
    s[0].append(6)
    
    print(id(s))
    return s

  = ([1,2,3],"a")

id(process(var))

id(var)

# Set
a = [1,2,3,4,4,5,5,6,5,6,7]

len(a)

st = set([[1]])

st.add(10)
st.pop()
st.remove(189)

st1 = {1,2,3,4,6}
st.union(st1)
st.intersection(st1)
st.difference(st1)
st.discard(17)


# dict

d = {}
d[[1,2,3]] = 'ravi'
d['names'] = 'ravi1'
d.keys()
d.values()
d.items()
d.get("hh")
d['hh']

'name' in d.keys()

d.pop('name')
d.popitem()
d.update({'name':'uday'})
d.fromkeys(['name','names'])



def fun():
    print('fgdfgfdf')

fun()

fun = lambda : 'hii'
fun()


# break,continue,pass




# context menager
with open('tetx.txt','a') as f:
    f.write("chal try karate hai \n")

with open('tetx.txt','r') as f:
    f.write("hdsghas")

f = open('tetx.txt','r')
f.read()
f.close()

f = open('tetx.txt','r')
f.readline()
f.close()

with open('tetx.txt','r') as f:
    v = True
    while v:
        v = f.readline()
        print(v)







