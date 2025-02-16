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
        pass