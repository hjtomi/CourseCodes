import datetime
import random
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    year = datetime.date.today().year
    return render_template("index.html", random_number=random_number, year=year)


@app.route("/guess/<name>")
def guess(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    age = response.json()["age"]
    response = requests.get(f"https://api.genderize.io?name={name}")
    gender = response.json()["gender"]

    return render_template("guess.html", age=age, gender=gender, name=name)


@app.route("/blog/<num>")
def blog(num):
    print(num)
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)

