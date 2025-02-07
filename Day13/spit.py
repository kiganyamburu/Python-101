csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']
print(friends_list)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise


csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'

# Step 1: Split the string by ':'
parts = csv.split(':')

# Step 2: Split the first part by ',' to get the names before the colon
names_before_colon = parts[0].split(',')

# Step 3: Split the second part by ';' to get the names after the colon
names_after_colon = parts[1].split(';')

# Step 4: Combine all the names into a single list
friends_list = names_before_colon + names_after_colon

# Print the final list
print(friends_list)