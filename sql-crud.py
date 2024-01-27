# using the ORM method - so copy & paste set up from sql-orm.py
from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#executing the instructions from the chinook database
db = create_engine("postgresql:///chinook")
base = declarative_base() # set base to declarative_base class


# CRUD: CREATE a table - decide table schema
# create a class-based model for the programmer table
class Programmer(base): # extend the declarative_base
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True) # primary key will increment automatically starting at 1
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of connecting to database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() sublass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records for our Programmer table
ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "F",
    nationality = "British",
    famous_for = "First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

morgan_oleary = Programmer(
    first_name="Morgan",
    last_name="O'Leary",
    gender="F",
    nationality="American",
    famous_for="Determination"
)

# add each instance of our programmers to our table using our current session
## this will add each programmer each time the file is run unleass commented out (ex. 6 lines of ada)
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(morgan_oleary)

# # commit our session to the database
# session.commit()


# CRUD: UPDATE
# updating a single record | .first() gets only one specific record
# define a query:
#programmer = session.query(Programmer).filter_by(id=12).first()
# define which columns need updating:
#programmer.famous_for = "World President"

# commit our session to the database
#session.commit()

# updating multiple records (query all programmers > already using that variable)
# people = session.query(Programmer)
# # update each record at the same time so iterate over each record w/ a for loop
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()    # commit each update within the loop


# CRUD : DELETE
# deleting a single record (user might not know 'id' so use Python input fields to prompt user to find a specific person from the table)
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# # defensive programming
# if programmer is not None:
#     print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")


# delete multiple/all records
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()


# CRUD: READ
# query the database to find all programmers (named variable)
programmers = session.query(Programmer) # query the Programmer table
# create a for loop for this list of programmers 
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | " # separate each item with a vertical bar/pipe
    )