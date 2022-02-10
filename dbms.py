#! /usr/bin/python
import sqlite3
conn=sqlite3.connect("Multimedia.db")
cursor = conn.cursor()

def create():
    cursor.execute("CREATE TABLE Movies(Name TEXT, year TEXT,quality TEXT)")
    cursor.execute("CREATE TABLE TVshows(Name TEXT, year TEXT,quality TEXT)")
    cursor.execute("CREATE TABLE Anime(Name TEXT,alternate_name TEXT , year TEXT,quality TEXT)")
    cursor.execute("CREATE TABLE AnimeMovies(Name TEXT,alternate_name TEXT , year TEXT,quality TEXT)")
#run the below line only once
def drop():
    cursor.execute('DROP TABLE IF EXISTS Movies')
    cursor.execute('DROP TABLE IF EXISTS TVshows')
    cursor.execute('DROP TABLE IF EXISTS Anime')
    cursor.execute('DROP TABLE IF EXISTS animeMovies')#comment this when the database is once perfectly created because it deletes the information
#for overwrighting everytime
#drop()
#create()
def close():
    conn.commit()
    cursor.close()

#Adding
def add_movie(Name,year,quality):
    cursor.execute("INSERT INTO Movies (Name,year,quality) VALUES(?,?,?) ",(Name,year,quality))
def add_ts(Name,year,quality):
    cursor.execute("INSERT INTO TVshows (Name,year,quality) VALUES(?,?,?) ",(Name,year,quality))
def add_anime(Name,alternate,year,quality):
    cursor.execute("INSERT INTO Anime (Name,alternate_name,year,quality) VALUES(?,?,?,?) ",(Name,alternate,year,quality))
def add_AnimeMovie(Name,alternate,year,quality):
    cursor.execute("INSERT INTO AnimeMovies (Name,alternate_name,year,quality) VALUES(?,?,?,?) ",(Name,alternate,year,quality))
#lists
def AllMovie():
    cursor.execute("SELECT * FROM MOVIES")
    movies = cursor.fetchall()
    for movie in movies:
        name,year,quality = movie
        print(name,'-',year,'-',quality)       
def AllTvshow():
    cursor.execute("SELECT * FROM TVshows")
    shows = cursor.fetchall()
    for show in shows:
        name,year,quality = show
        print(name,'-',year,'-',quality)
def AllAnime():
    cursor.execute("SELECT * FROM Anime")
    Animes = cursor.fetchall()
    for Anime in Animes:
        name,alternate,year,quality = Anime
        print(name,'-',alternate,'-',year,'-',quality)
def AllAnimeMovie():
    cursor.execute("SELECT * FROM AnimeMovies")
    AnimeMovies = cursor.fetchall()
    for AnimeMovie in AnimeMovies:
        name,Alternate,year,quality = AnimeMovie
        print(name,'-',Alternate,'-',year,'-',quality)
#columns
def Movielist():
    cursor.execute("Select Name FROM Movies")
    movies = cursor.fetchall()
    movieNames=list((str(elements).strip()[2:-3]+'' for elements in movies))
    return movieNames
def TSlist():
    cursor.execute("Select Name FROM TVshows")
    TvshowNames = cursor.fetchall()
    TvshowNames=list((str(elements).strip()[2:-3]+'' for elements in TvshowNames))
    return TvshowNames
def Animelist():
    cursor.execute("Select Name FROM Anime")
    AnimeNames = cursor.fetchall()
    return AnimeNames
def Amlist():
    cursor.execute("Select Name FROM AnimeMovies")
    Animemovies = cursor.fetchall()
    return Animemovies
def searchMovie(Name):
    movielist = Movielist()
    for movie in movielist:
        if movie == Name:
            index= movielist.index(movie)
            print(index)
            cursor.execute("Select * FROM Movies")
            info = cursor.fetchall()[index]
            print(info)
        elif movie.startswith(Name[0]):
            index = movielist.index(movie)
            cursor.execute("Select * FROM Movies")
            info = cursor.fetchall()[index]
        elif movie.endswith(Name[len(Name)-1]):
            index = movielist.index(movie)
            cursor.execute("Select * FROM Movies")
            info = cursor.fetchall()[index]
            print(info)       



