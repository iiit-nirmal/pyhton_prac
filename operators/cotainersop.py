import operator as op

l1=[1,2,3,4] ## indexing starting from 0
## getitem
print(op.getitem(l1,3))
print(op.getitem(l1,slice(1,4))) ##  slice(a,b)  -- [a,b)

## setitem
op.setitem(l1,2,6)
op.setitem(l1,slice(1,2),[4])

## delitem
op.delitem(l1,1)
op.delitem(l1,slice(2,3))

## travessing the list
print("list")
for x in l1:
    print(x)

l2 = [90,23,1]
l3 = op.concat(l1,l2)
print(op.contains(l3,l1))

######### bitwise operation

a=1
b=0
print(op.and_(a,b))
print(op.or_(a,b))
print(op.xor(a,b))
print(op.invert(a))

