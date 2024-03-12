import random

class video:
    def __init__(self, title, date, species, plays=0):
        self.title = title
        self.date = date
        self.species = species
        self.plays = plays
    def __repr__(self):
        return self.title
    @property
    def play(self):
        self.plays += 1     

class series(video):
    def __init__(self, title, date, species, plays, ep, season):
        super().__init__(title, date, species, plays)
        self.ep = ep
        self.season = season
    @property
    def info(self):
        if self.season < 10 and self.ep > 9:    
            print(f"{self.title}, S0{self.season} E{self.ep} played {self.plays} times")
        if self.season < 10 and self.ep < 10:    
            print(f"{self.title}, S0{self.season} E0{self.ep} played {self.plays} times")
        if self.season > 9 and self.ep < 10:
            print(f"{self.title}, S{self.season} E0{self.ep} played {self.plays} times")
        if self.season > 9 and self.ep > 9:
            print(f"{self.title}, S{self.season} E{self.ep} played {self.plays} times")         

class movie(video):
    def __init__(self, title, date, species, plays):
        super().__init__(title, date, species, plays)
    @property
    def info(self):
        print(f"{self.title} ({self.date}) viewed {self.plays} times")        

Jaws = movie(title="Jaws", date=1997, species="movie", plays=0)
Shawshank_Redemption = movie(title="Shawshank Redemption", date=1994, species="movie", plays=0)
The_Godfather = movie(title="The Godfather", date=1972, species="movie", plays=0)
Pulp_Fiction = movie(title="Pulp Fiction", date=1994, species="movie", plays=0)
Fight_Club = movie(title="Fight Club", date=1999, species="movie", plays=0)
Inception = movie(title="Inception", date=2010, species="movie", plays=0)
The_Matrix = movie(title="The Matrix", date=1999, species="movie", plays=0)
Seven = movie(title="Seven", date=1995, species="movie", plays=0)
BB = series(title="Breaking Bad", date=2008, ep=4, season=1, species="series", plays=0)
GOT = series(title="Game Of Thrones", date=2011, ep=11, season=3, species="series", plays=0)
RM = series(title="Rick & Morty", date=2013, ep=9, season=6, species="series", plays=0)
The_Office = series(title="The Office", date=2005, ep=15, season=11, species="series", plays=0)
BCS = series(title="Better Call Saul", date=2015, ep=10, season=3, species="series", plays=0)

my_list = {Jaws, Shawshank_Redemption, The_Godfather, Pulp_Fiction, Fight_Club, Inception, The_Matrix, Seven, BB, GOT, RM, The_Office, BCS}

def get_movies():
        Movies = []
        for video in my_list:
            if video.species == "movie":
                Movies.append(video.title)
        print(sorted(Movies))
def get_series():
        Series = []
        for video in my_list:
            if video.species == "series":
                Series.append(video.title)
        print(sorted(Series))
def search(name):
    for video in my_list:
        if video.title == name:
            print(f"{video.title} is a {video.species} from {video.date} with {video.plays} views")    
def generate_views():
    i = random.choice(list(my_list))
    i.plays += random.randint(1,100) 
def generate_views10():
    for i in range(11):
        generate_views()
def top_titles(i):
    top = sorted(my_list, key=lambda video: video.plays, reverse=True)
    print(f"{top[:i]}")        
generate_views10()
top_titles(5)
BCS.info
search("Inception")