# http://hangar.runway7.net/python/packing-unpacking-arguments

## function for unpacking tuple
def func1(a,b,c):
    print(a,b,c)

## function for packing tuple
def func2(*arg):
    for x in arg:
        print(x)

# Driver code
# arglist = ['Hello', 'beautiful', 'world!']
# func1(*arglist) ### wrapping of a list
# func2('Hello', 'beautiful', 'world!')


##  function for unpacking dictionary
def fun(a, c, b): ## dictionaries values are passed based on matching key
    print(a, b, c)


# A call with unpacking of dictionary
d = {'a': 2, 'b': 4, 'c': 10}
fun(**d)

##  function for packing dictionary
def dfun2(**argdic):

    for k in argdic:
        print(argdic[k])
    ######### order not defined

dfun2(a=1,b=2,c=3)


#################################################################################

### packing -- list and dictionary (when size of list or dict is uncertain)

def pack_list(*args):
  for x in args:
      print(x)

l = pack_list(1,2,3)

def pack_dict(**args):
    for key in args:
        print(args[key])

l = pack_dict(a=1,b=2,c=3)

### unpacking -- list and dictionary

def unpack_list (a,b,c):
    print(a,b,c)

unpack_list(*[1,2,3])

def unpack_dict (a,b,c): ## a,b,c are keys
    print(a,b,c)

unpack_list(**{'a':1,'b':2,'c':3})
