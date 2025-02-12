names = ["john ClEEse", "Eric IDLE", "michael"]
names1 = ["graHam chapman", "TERRY", "terry jones"]

# combine the two lists

new_list = names + names1

for _ in range(2):
    new_list = input("Enter a name: ")
    new_list.append(new_list)

    for name in new_list:
        formatted_name = name.title()
        print(f"{formatted_name}! You are invited to the party o saturday")
