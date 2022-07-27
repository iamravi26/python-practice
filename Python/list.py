a = ""
b = ""
c = ""

id(a),id(b),id(c)

####################


a = 1
b = 1
c = 1

id(a),id(b),id(c)



####################


a = []
b = []
c = []

id(a),id(b),id(c)



####################


a = []
b = a
c = b

id(a),id(b),id(c)



####################


a = ()
b = a
c = b

id(a),id(b),id(c)


####################


a = (1)
b = (1)
c = (1)

id(a),id(b),id(c)




#########

a = {}
b = {}
c = {}

id(a),id(b),id(c)


#########

a = {1}
b = {1}
c = {1}

id(a),id(b),id(c)




'''
Variable Equality

== ,is

'''

a = 10
b = 10
id(a),id(b)
a == b
a is b

##################

a = 1000
b = 1000
id(a),id(b)
a == b
a is b


##################

a = None
b = [None]
id(a),id(b[0])


a = 0
b = [0]
id(a),id(b[0])


a = True
b = [True]
id(a),id(b[0])






