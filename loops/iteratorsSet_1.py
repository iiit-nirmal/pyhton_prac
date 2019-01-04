import itertools
import operator as op

# initializing list 1
li1 = [1, 4, 5, 7]

# initializing list 2
li2 = [1, 6, 5, 9]

# initializing list 3
li3 = [8, 10, 5, 4]

## using accumulate()
print("addition operation",list(itertools.accumulate(li1,op.add)))

## using chain
print("chain operation",list(itertools.chain(li1,li2,li3)))

## using chain.from_iterable
list4 = [li1,li2,li3]
print("iterable chain",list(itertools.chain.from_iterable(list4)))

## compress using boolean list
boolean_list = [True,False,True,True]
print("compress:", list(itertools.compress(li3,boolean_list)))

## dropwhile and filter false

print(list(itertools.dropwhile(lambda x:x%2==0,li2)))
print(list(itertools.filterfalse(lambda x:x%2==0,li2)))




