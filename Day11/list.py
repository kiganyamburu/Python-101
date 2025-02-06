friends = ["John", "Michael", "Terry", "Eric", "Graham"]
cars = [911, 130,328, 535, 740, 308] 
print(friends)
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)
friends.reverse()
print(cars)
print(min(cars))
print(max(cars))
print(sum(cars))

# cars.sort()
# print(cars)

friends.append("Terry")
print(friends)
friends.insert(1, "Jim")

print(friends)

friends.sort()


fruits = ["mangoes", "bananas", "apples"]
fruits.append("avocado")
print(fruits)

for avocado in fruits:
    print(avocado)


#  coping a list
room = ["table", "chair", "bed", "wardrobe"]
new_room = room.copy()
print(new_room)