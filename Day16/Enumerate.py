print("python101 - Enumerate")
friends = ["Brian", "Judith", "Reg", "Loretta", "Colin"]

i = 0
# for friend in friends:
#     print(i, friend)
#     i = i + 1

for num, friend in enumerate(friends, 1):
    print(num, friend)
