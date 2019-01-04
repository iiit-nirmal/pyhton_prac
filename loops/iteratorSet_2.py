## infinite iterators
import itertools as itert

## count
# print(list(itert.count(2,1))) # print infinitely from start 2 with step 1

## cycle
it = [1,2,3]
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

###