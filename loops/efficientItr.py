cars = ["Aston", "Audi", "McLaren"]

#Enumerate is built-in python function that takes input as iterator, list etc and returns a tuple containing index and data at that index in the iterator sequence.
#For example, enumerate(cars), returns a iterator that will return (0, cars[0]), (1, cars[1]), (2, cars[2]), and so on.

for k,v in enumerate(cars):
    print(k,v)

#Enumerate takes parameter start
#which is default set to zero. We can change this parameter to any value we like. In the below code we have used start as 1.

for k,v in enumerate(cars,start=2):
    print(k,v)

cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS", "Car Repair Kit",
               "Dolby sound kit"]

# Combining lists and printing
for c, a in zip(cars, accessories):
    print("Car: %s, Accessory required: %s" % (c, a))

# Python program to demonstrate unzip (reverse
# of zip)using * with zip function

# Unzip lists
l1, l2 = zip(*[('Aston', 'GPS'),
               ('Audi', 'Car Repair'),
               ('McLaren', 'Dolby sound kit')
               ])

# Printing unzipped lists
print(l1)
print(l2)