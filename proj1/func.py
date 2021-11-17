def fun(a,b,c=0):

    return a + b + c


print(fun(3,4,5))
print(fun(b=2,c=4,a=5))


data = (2,7,9)
print(fun(*data))
print(*data, sep='__')
print([*data])
another = {'a':5, 'b':6, 'c':7 }
print(fun(**another))
print(**another)