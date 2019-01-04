## continue returns control the begining of loop
for letteres in 'geeksgeeks':
     if letteres == "e" or letteres == "s":
         continue
     print('character:',letteres)

## break returns control to the end of loop
for letteres in 'geeksforgkees':
    if letteres == "e" or letteres == "s":
        break
    print('character:', letteres)

## pass is used to write emplty loops
print("pass...")
for letteres in 'geekdsadsasd':
    pass
print(letteres)

