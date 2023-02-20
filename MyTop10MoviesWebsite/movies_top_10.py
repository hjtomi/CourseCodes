import os

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

TMDB_API_KEY = os.environ.get("TMDB_API_KEY")

db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
db.init_app(app)
Bootstrap5(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.String, nullable=True)
    ranking = db.Column(db.String, nullable=True)
    review = db.Column(db.String, nullable=True)
    img_url = db.Column(db.String, nullable=True)


with app.app_context():
    db.create_all()


class FormEdit(FlaskForm):
    rating = StringField('Rating', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    button = SubmitField('Done')


class FormAdd(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    button = SubmitField('Add Movie')


@app.route("/")
def home():
    movies = db.session.query(Movie).all()
    movies = sorted(movies, key=lambda x: float(x.rating), reverse=True)

    for i, movie in enumerate(movies):
        movie.ranking = i + 1

    db.session.commit()

    return render_template("index.html", movies=reversed(movies))


@app.route("/add")
def add():
    form = FormAdd()
    return render_template('add.html', form=form)


@app.route("/select", methods=["GET", "POST"])
def select():
    title = request.form["title"]
    response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={title}")
    movies = response.json()["results"]

    return render_template('select.html', movies=movies)


# --- We differantiate 2 ids, the movie id and the SQL database id --- #
@app.route("/fetchdata/<int:movie_id>", methods=["GET", "POST"])
def fetch_data(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}")
    movie_data = response.json()
    movie = Movie(
        title=movie_data["original_title"],
        year=movie_data["release_date"],
        description=movie_data["overview"],
        rating="None",
        ranking="No.#",
        review="None",
        img_url=f"https://image.tmdb.org/t/p/original{movie_data['poster_path']}"
    )
    db.session.add(movie)
    db.session.commit()

    return redirect(url_for('edit', iden=movie.id))


@app.route("/edit/<int:iden>", methods=["GET", "POST"])
def edit(iden):
    if request.method == "POST":
        movie = db.get_or_404(Movie, iden)
        movie.rating = request.form["rating"]
        movie.review = request.form["review"]
        db.session.commit()

        return redirect(url_for('home'))

    form = FormEdit()
    return render_template('edit.html', movie=db.get_or_404(Movie, iden), form=form)


@app.route("/delete/<int:iden>", methods=["GET", "POST"])
def delete(iden):
    db.session.delete(db.get_or_404(Movie, iden))
    db.session.commit()

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
