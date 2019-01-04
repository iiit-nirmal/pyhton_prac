## infinite iterators
import itertools as itert

## count
# print(list(itert.count(2,1))) # print infinitely from start 2 with step 1

## cycle
it = [1,2,3]
it1 = [4,5,6]
li1 = [ (1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10 , 1) ]
# itert.cycle(it) ## print it elements in cycle infinitely

## repeat
print(list(itert.repeat(2,100))) ## repeat value 2 till 100 times

## permutation and combination
it2 = [4,5,6]
print(list(itert.permutations(it,2))) ## permuation for list with group size 2
print(list(itert.combinations(it,2))) ## combinations for list with group size 2
print(list(itert.combinations_with_replacement(it,2))) ## combinations for list with group size 2 with replacment

### cartesian product with two iterators
print("product :",list(itert.product(it,it2)))

### islice -- slicling iterable object
print("slice",list(itert.islice(it,1,3,1)))

### starmap -- apply a fuunction on tuple list
print("star map:",list(itert.starmap(min,li1)))

### takewhile -- prints the values of iterable till it is false
print("takewhile:",list(itert.takewhile(lambda x:x%2==0,it)))

### tee -- splits the container into no of iterators
print("tee:",list(itert.tee(it,2)))

it_ = itert.tee(it,2)
for  l in range(0,2):
      print(list(it_[l]))

## zip-longest

print("zip_longest",print(list(itert.zip_longest(it,it1,"_"))))