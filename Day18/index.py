
# my_file = open("greeting.txt","r")
# print(my_file.read(10))
# print(my_file.readlines())
# print(my_file.readlines())

# line_by_line = my_file.readline()
# line_by_line = my_file.readline().splitlines()
# print("readline: ", line_by_line)
# print("splitlines: ", line_by_line)

# my_file.close()
#  or 

# context manager

with open("friends.csv","r") as f:
    print(f.read())
    friends = f.read().splitlines()
    print(friends)
    for friend in friends:
        friend = friend.split(', ')
        name = friend[0]
        year = int(friend[1].strip())
    print(f"in 2030 {name} will be {2030 - year} years old")