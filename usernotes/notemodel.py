""" database dependencies to support Users db examples """
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate

from __init__ import app

# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
# Define variable to define type of database (sqlite), and name and location of myDB.db
dbURI = 'sqlite:///modelnotes/myDB.db'
# Setup properties for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
# Create SQLAlchemy engine to support SQLite dialect (sqlite:)
db = SQLAlchemy(app)
Migrate(app, db)


# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Users_notes(db.Model):
    # define the Users schema
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    subject = db.Column(db.String(255), unique=True, nullable=False)
    notes = db.Column(db.String(255), unique=False, nullable=False)


    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, subject, notes):
        self.name = name
        self.subject = subject
        self.notes = notes

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "userID": self.userID,
            "name": self.name,
            "subject": self.subject,
            "notes": self.notes
        }

    # CRUD update: updates users name, password, phone
    # returns self
    def update(self, name, subject, notes):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(notes) > 0:
            self.notes = notes
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing section"""


def model_tester():
    print("--------------------------")
    print("Seed Data for Table: users")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""
    u1 = Users_notes(name='Thomas Edison', subject="AP Stats", notes="p-values come from using normal cdf on calculator")
    u2 = Users_notes(name='Nicholas Tesla', subject="AP CSP", notes="an 'if' loop needs a condition")
    u3 = Users_notes(name='Alexander Graham Bell', subject="AP US History", notes="Dec 7 1941 was when Japan attacked Pearl Harbor, which is why the US joined WWII")
    u4 = Users_notes(name='Eli Whitney', subject="AP Calculus AB", notes="the derivative of position is velocity")
    # U7 intended to fail as duplicate key
    u7 = Users_notes(name='Eli Whitney', subject="AP Calculus AB", notes="the derivative of position is velocity")

    table = [u1, u2, u3, u4, u7]

    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()


def model_printer():
    print("------------")
    print("Table: users with SQL query")
    print("------------")
    result = db.session.execute('select * from users_notes')
    print(result.keys())
    for row in result:
        print(row)


if __name__ == "__main__":
    model_tester()  # builds model of Users
    model_printer()