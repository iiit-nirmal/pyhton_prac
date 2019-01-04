#### airthmetic op-erators
print(1+2)
print(1-2)
print(2/3)  # float value of division
print(2//3) # floor value of division
print(2 %3) # modulus value of division

## relational operator -- return True/False

print(1 > 2)
print(1 >= 2)
print(2 == 3)
print(2 !=3)
print(2 <=3)

## logical operator -- applied on boolean and return True/False

print(1 and 2) #return 2
print(1 or 2)  # return 1
print(not 3)   # return false

## bitwaise operator

print(1&2)
print(1|2)
print(~1)

## identify operator
a = 1
b = 2
print( a is b) ## a and b same located
print(a is not b )

## membership operator -- dict,list,set,tuple

l = (1,2,3)
dic = {'a':1,'b':2}

print(1 in l)
print('a' in dic)

## ternary operator --

a,b = 10,20

min = a if a >b else b
max = a if a <b else b
print(min)
print(max)

#### or with tuples
print("max ::",(a,b) [a<b])
print("min ::",(b,a) [a<b])

#### with dict
print("max::", {True:a,False:b} [a>b])
print("min::", {True:b,False:a} [a>b])

## any/all -- return true/false
## True if any item is true

print(any([True,False]))
print(any([True,True]))