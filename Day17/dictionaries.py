# they store key and pair value
# people = {
#     "John": 20,
#     "Ken": 21,
# }
# print(type(people))


# dictionaries are mutable so that means we can easily modify them

movie = {
    "title": "Inception",
    "year": 2010,
    "genre": "Action",
    "cast": ["Peter", "John", "Erich", "george", "Terry"],
}
for key, value in movie.items():
    print(key, value)

print(movie.get("genre", "not found"))
# get method is for getting key form the dictionary
