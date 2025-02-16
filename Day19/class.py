print("Classes & objects")
# classes are like a blueprint 
# object are the actual things built
# variables re the attributes
# funtions are the methods


class Movie:
    def __init__(self, title, year,imdb_score, have_seen):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen
        
    def nice_print(self):
        print("Title: ",self.title)
        print("Year of production: ",self.year)
        print("IMDB score: ",self.imdb_score)
        print("I have seen it: ",self.have_seen)
              
film_1 = Movie("Life of brian", 1979,8.1, True)
film_2 = Movie("The Holy Grail", 1975,8.2, True)

films = [film_1, film_2]

