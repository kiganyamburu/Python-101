#  Dictionary comprehensions 
movies = ["And now for something completely Different", "Monty Python and the Holy Grail","monty Python's life of Brian", "Monty python live at the Hollywood Bowl","Monty Python's the meaning of life", "Monty Python live (mostly)"]
year = [1971, 1975,1979, 1982, 1983, 2014]
names = ["John", "Eric", "michael", "Graham", "Terry", "TerryG"]
print(list(zip(movies, year)))
# give me a dict("movies": year) for each movies, year in zip(names, names)
new_dict = dict()
for movie, year in zip(names, names):
    new_dict[movie] = year
print(new_dict)
new_dict = {movie:year for movie, year in zip(movie, year)}
print(new_dict)