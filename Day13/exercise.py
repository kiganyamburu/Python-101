#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

if {"Eric", "John"} <= friends:
    print("Both Eric and John are in my friends set")
else:
    print("Both Eric and John are not in my friends set")
    
print(friends.union(my_friends))
print(friends.intersection(my_friends))
print(friends.difference(my_friends))

result = friends ^ my_friends
print("symmetric difference(^):", result)

new_set = friends | my_friends
print(new_set)



