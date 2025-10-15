students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": "Hone"},
    {"name": "Luna", "house": "Ravenclaw", "patronus": "Hare"},
    {"name": "Cedric", "house": "Hufflepuff", "patronus": "Giant"}
]


for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")