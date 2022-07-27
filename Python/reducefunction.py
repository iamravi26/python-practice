from audioop import avg
from numpy import average
import math


maxvalue = lambda a,b : a if a> b else b

sequence= [5, 8, 6, 10, 9]
def max_sequence(sequence):
    result = sequence[0]
    for e in sequence[1:]:
        result = maxvalue(result, e)
    return result

max_sequence(sequence)
max(sequence)
min(sequence)
sum(sequence)


from functools import reduce
reduce(lambda a,b:a if a>b else b,sequence)
reduce(lambda a,b:a if a<b else b,sequence)
reduce(lambda a,b:a+b,sequence)
reduce(lambda a,b:a+b,[],100)