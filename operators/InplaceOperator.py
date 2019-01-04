import operator as op

############ immutable targerts
a =10
b= 10

######### a+b
op.add(a,b)
print(a)

######### a+b
op.iadd(a,b)
print(a)

########### mutable targets
a=[1,2,3,4]

######### a+b
op.add(a,[5])
print(a)

########## a+=b
op.iadd(a,[6])
print(a)
