# can forget the Table import as we are creating Python classes not tables
from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

# import declarative base from sqlalchemy declarative extension
# classes will subclass the declarative_base : classes made will extend from main class w/in the ORM
from sqlalchemy.ext.declarative import declarative_base

# import session maker class from the ORM
# instead of making connection to the database directly, ask for a session
from sqlalchemy.orm import sessionmaker

#executing the instructions from the chinook database
db = create_engine("postgresql:///chinook") # using postgres server on local host to connect to database

# This new 'base' class will essentially grab the metadata that is produced by our database
# table schema, and creates a subclass to map everything back to us here within the 'base' variable.
base = declarative_base() # set base to declarative_base class

# add tables before Session is created but after the base is declared
# create a class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instead of connecting to database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)

#connect to the database
# opens an actual session by calling the Session() sublass defined above
session = Session()

# create database sublass & generate all metadata
# creating the database using declarative_base subclass
base.metadata.create_all(db)

# now its set up so we can start to build our class based models ^^^
# build a normal Python object that sublassess 'base' ^^^

# Query 1 - select all records from the "Artist" table
# use existing session instance & query the Artist class (everything in table above)
# artists = session.query(Artist)
# for artist in artists:          # iterate over the results found
#     # print each column using dot notation on for loop & separate each item with the Python separator |
#     print(artist.ArtistId, artist.Name, sep=" | ")   

# Query 2 - select only the "Name" column from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Query 3 - select only "Queen" from the "Artist" table
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )

