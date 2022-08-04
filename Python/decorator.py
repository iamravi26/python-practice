# Closer 
#decorator





from dis import dis
from functools import wraps
from re import L
from textwrap import wrap


def outer():
    a = 100
    x = 'python'
    def inner():
        #a = 10 # local variable
        print(a)
        print("{0} rocks!".format(x))
    return inner

fn = outer()
fn.__code__.co_freevars
fn.__closure__
fn()



x=100
def outer():
    l='hello'
    def inner_1():
        print(l)
    
    def inner_2():
        nonlocal l
        l="ravi"
    return inner_2,inner_1

        

a=outer()
print(a)
a[0]()
a[1]()



def counter():
    count =0
    def inner():
        nonlocal count
        count+=1
        print(count)
    return inner

ct = counter()
ct()



# decorator

def counter_decorator(fn):
    count =0
    def inner(*args,**kwrgs):
        '''
        This is the inner function
        '''
        nonlocal count
        count +=1
        print(f'Function caller count : {count}')
        return fn(*args,**kwrgs)
    inner.__doc__ = fn.__doc__ #coz add ka docstring & name overwrite kar de raha tha to avoid it we did this
    inner.__name__ = fn.__name__
    return inner

# first method

def add(a,b):
    '''
    this function add two numbers
    '''
    return a+b
add.__doc__
add.__name__
add = counter_decorator(add) #We essentially modified our add function by wrapping it inside another 
# function that added some functionality to it
# We also say that we decorated our function add with the function counter
# And we call counter a decorator function

add.__doc__
add.__name__
add(2,8)

# second method to apply decorator on add function
@counter_decorator
def sub(a,b):
    return a-b
sub(9,7)

from functools import wraps

def counter_decorator(fn):
    count =0
    @wraps(fn)  #to fix the metadata of inner function#it is actually a built in decorator
    def inner(*args,**kwrgs):
        '''
        This is the inner function
        '''
        nonlocal count
        count +=1
        print(f'Function caller count : {count}')
        return fn(*args,**kwrgs)
    return inner

@counter_decorator
def sub(a,b):
    '''
    this function add two numbers
    '''
    return a-b
sub(9,7)

sub.__doc__
sub.__name__

# parametarise decorator 

def timed(fn):
    from time import perf_counter
    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(15):
            start = perf_counter()
            result = fn(*args, **kwargs)
            total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / 10
        print(avg_elapsed)
        return result
    return inner

@timed
def add(a,b):
    return a+b 


def timed(repreat):
    def desc(fn):
        from time import perf_counter
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(repreat):
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / repreat
            print(avg_elapsed)
            return result
        return inner
    return desc

@timed(15)
def add(a,b):
    return a+b 

add(6,10)


def decorator1(fn):
    print('decorator1')
    def inner(*args,**kwrgs):
        '''
        This is the inner function
        '''
        print('decorator1 start ')
        res = fn(*args,**kwrgs)
        print('decorator1 end')
        return res
        
    return inner

def decorator2(fn):
    print('decorator2')
    def inner(*args,**kwrgs):
        '''
        This is the inner function
        '''
        print('decorator2 start ')
        res = fn(*args,**kwrgs)
        print('decorator2 end')
        return res
        
    return inner


@decorator2
@decorator1
def display():
    print('Hello')

display()



@decorator1
@decorator2
def display():
    print('Hello')

display()







