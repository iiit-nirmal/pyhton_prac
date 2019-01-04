## generate fuction yield rather return and return generator object.
def fib(limit):

    a,b =0,1

    while a < limit:
        yield a
        a ,b = b,a+b

## here fib returns a generater object
x =fib(10)

## you can use next() function or for loop to get items in generator object 
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# for t in x:
#     print(t)


