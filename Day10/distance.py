# create a distance converter converting Km to miles
# Take two inputs from users:Their first name and the distance in Km
# Print: Greet user by name and show Km, and miles values
# 1 mile id 1.609 lm
# hint: use correct types for calculation and print 
# Did you capitalize the name

name = input("Enter your first name: ")
distance_km = float(input("Enter the distance in Km: "))
distance_miles = distance_km / 1.609
print(f"Hello {name.capitalize()}, {distance_km} Km is equal to {distance_miles} miles")


