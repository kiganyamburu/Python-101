python = {
    "John": 35,
    "Eric": 36,
    "Michael": 35,
    "Terry": 38,
    "Graham": 37,
    "TerryG": 34,
}

holy_grail = {
    "Arthur": 40,
    "Galahad": 35,
    "Lancelot": 39,
    "Knight of NI": 40,
    "Zoot": 17,
}
life_of_brian = {
    "Brian": 33, 
    "Reg": 35, 
    "Stan/Loretta": 32, 
    "Biccus Diccus": 45
}

# dictionary are key sensitive and
# dictionary are unordered and can have duplicate values but not keys.
print("Arthur" in holy_grail)
if "Arthur" not in python:
    print("He's not here")
    
# concatenating dictionary
people = {}
people1 = {}
people2 = {}

# first method is the update method
people.update(python)
print(people)



