from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html', books=db.session.query(Book), has_books=db.session.query(Book).first())


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')


@app.route("/edit/<int:iden>", methods=["GET", "POST"])
def edit(iden):
    if request.method == "GET":
        return render_template('edit.html', book=db.get_or_404(Book, iden))

    elif request.method == "POST":
        new_rating = request.form['rating']
        book = db.get_or_404(Book, iden)
        book.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))


# Made with the request.args.get("") method to showcase this possibility!
@app.route("/delete")
def delete():
    db.session.delete(db.get_or_404(Book, request.args.get("id")))
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

