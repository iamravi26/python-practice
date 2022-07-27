t = ([1,2,3],[4,5,6])
id(t)
t[0].append(5)
print(t)

def func1(a,b,*c):
    try:
        add=a+b+c
    except Exception as e:
        print(e)
        add=a+b
    for i in c:
        print(add)
        add = add+i
    return add
    
a=func1(10,20,30,40)    
print(a)

def func1(*args,**kwargs):
    print(args)
    print(kwargs)

func1(1,2,6,x=3,y=4)

s= "iittII Am learning python"
#s.lower()
#s.capitalize()   "IittII Am learning python"
#s.upper()    'IITTII AM LEARNING PYTHON'
#s.split() ----['iittII', 'Am', 'learning', 'python']
#s.startswith('h')  False
#s.endswith('you')  False 
#s.strip('i')   'ttII Am learning python'
#s.count('t')  3
#s.index('a')  12 a is at the 12 position counting from 0
#s.find('i')   0
#s.isdigit()  # false coz its not a digit string
#'434'.isdigit() true coz 434 is digit
#s.lstrip()   spaces hata deta hai left side se
#s.replace('Am','hiiiiiiiiiiii')
#s.__dir__()
#print(s)