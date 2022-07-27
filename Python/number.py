

import ctypes
import sys

a = 5
a = 10

sys.getrefcount(a)


ctypes.c_long.from_address(id(a)).value

import gc
gc.collect()

a = 10
type(a)
a =""
type(a)

# a = [] -->  list()
# b = () --> tuple()
# c =set()
# d = {} --> dict()

# IMMUTABLE 

i = 10
id(i)

i = 11
id(i)


st = "10"
id(st)
st = "110"
id(st)

tp = (1,2,3)
id(tp)
tp = (1,2,3,4)

id(tp)


#Mutable

lt= [1,3,4]
id(lt)

lt.append(3)
lt
id(lt)

id(lt[3])


st = {1,2,3}
id(st)

st.add(10)
st

id(st)

tp  = ([1,2,3],[3,4,5])
id(tp)

id(tp[0])
tp[0].append(8)
tp





dt = {1:1,2:2}
id(dt)


dt[5]  =5

id(dt)



t = ([1,2,3],[4,5,6])
id(t)

t[0].append(5)









