a= "1223a23"
b = "1211321"

############# to integer with base(for string only)
print(int(a,16)) # convert a with base 10(for string only)

####### integer to hex,oct
print(hex(23))
print(oct(32))

############  to float
print(float(b)) # convert to float

############ to character to ascii value (ord)
print(ord('a')) # convert character to corresponding ascii value(integer)

########### integer to hex,oct,str
a = 12123312908423
print(hex(a)) # convert a into hex (base 16)
print(oct(a)) # convert a into octal (base 8)
print(str(a)) # copnvert int to str

########## to list,tuple,set
a= [1,2,3]
print(tuple(a)) # (1,2,3) # to tuple
print(list(a))  # [1,2,3] # to list
print(set(a))   # {1,2,3} # to set

#### tuples to dict
tuples = (('a',1),('b',2),('c',3))
print(dict(tuples))

