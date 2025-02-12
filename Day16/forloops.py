for letter in range(1, 15, 3):
    print(letter)
print("for loop done!")


# working with loops in a list of name

for name in [
    "john",
    "Terry",
    "Eric",
    "Michael",
    "George",
]:
    print(name)

# working on a list of names
friends = ["kim", "John", "Joy", "dan"]
for index in range(len(friends)):
    print(friends[index])


#  Break out of
friends = ["John", "Terry", "Eric", "Michael", "George"]
for friend in friends:
    if friend == "Eric":
        print("Found" + friend + "!")
        break
    print(friend)

print("For Loop done!")

# continue
friends = ["John", "Terry", "Eric", "Michael", "George"]
for friend in friends:
    if friend == "Eric":
        print("Found" + friend + "!")
        continue
    print(friend)

print("For Loop done!")
