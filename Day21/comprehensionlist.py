numbers = [1,2,3,4,5,6,7,8,9]
# give me a list with num squared for each num in numbers

new_lists = []
for num in numbers:
    new_lists.append(num*num)
print(new_lists)

new_lists = [num for num in numbers if num % 2 == 0]
print(new_lists)
# even number

new_lists = [num for num in numbers if num % 2 == 1]
print(new_lists)
# odd number 
# give me a list with num for each num in numbers if num is even

new_lists = [num for num in numbers if num % 2 != 1]
print(new_lists)

new_lists = [num for num in numbers if num % 2 != 0]
print(new_lists)

# using a filter amd a lambda
new_lists = filter(lambda num:num % 2 ==0, numbers)
print(new_lists)

#  i want a (Letter, Num) pair for each letter in "spam" and each number "0123"

new_lists = []
for letter in "spam":
    for num in range(4):
        new_lists.append((letter,num))
print(new_lists)

new_lists = [(letter,num) for letter in "spam" for num  in range(4)]
