from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


# create data
with app.app_context():
    db.session.add(Book(title="x", author="y", rating="z"))


with app.app_context():
    # get record by id
    print(db.get_or_404(Book, 3))
    # get record by data
    book = db.first_or_404(db.select(Book).filter_by(title="Harry Potter and the chamber of secrets"))
    # modify data
    book.title = "hagrid"
    # delete record
    db.session.delete(book)
    # commit the changes, like in gitHub
    db.session.commit()


# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
