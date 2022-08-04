#atleast we need "try & except" or "try & finally" otherwise it will show syntax error


try:
    v = 100/2
    print(v)
except ZeroDivisionError:
    print('Number cannot be divided by 0')
except NameError:
    print('variable define nahi h')

except Exception as e :#if else shows error then only it will execute except 
    print(f'Exception......:{e}')
else:    #if try get executed then only else get execute
    print('Else........')
finally:#it will get executed every time
     print('Finalyy........')
     a=45+45
     print(a)


issubclass(NameError,Exception)
