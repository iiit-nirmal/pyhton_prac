### iteratioons in python

cars = ["aston","audi","maruti"]

## iterators of lists,dict, n dims array
for x in cars:
    print(x)

## iterators of containers using range with len
for x in range(len(cars)):
    print(cars[x])

## iteration using enumerate(bulit in functions that takes iterator and returns a tuple constaining index and data at that index)
t = enumerate(cars) ## returns an enumerate object as (0,cars[0]),(1,cars[1]),(2,cars[2])
print(t)

for x in enumerate(cars):
    print(x[0],x[1])
 ## here index starts from 0 by default but we can set using start

for x in enumerate(cars,start=2):
    print(x[0],x[1])

############## zipping
## zip function used to combine similar type iterators (list-list or dict-dict) data items at ith position
## items of larger length iterators are ignored
accessories = ["GPS", "Car Repair Kit",  "Dolby sound kit"]

for c,a in zip(cars,accessories):
    print(c,a)

############## unzipping
l1,l2 = zip(*[("aston","GPS"),("audi","Car Repair Kit")])
print(l1)
print(l2)

############## dict iterators
dict_ = {"geeks" : "for", "only" : "geeks" }

##### using items in python3 and iteritems in python2
for k,v in dict_.items():
    print(k,v)

##### using key
for k in dict_:
    print(k,dict_[k])

##### sorted(built in function) is used to print container in sorted order. but it dose not sort the elements
lis = [ 1 , 3, 5, 6, 2, 1, 3 ]
for x in sorted(lis):
    print(x,end=" ")

print(end="\n")
##### reveresed is used to print container in reverse order
for x in reversed(lis):
    print(x,end=" ")
