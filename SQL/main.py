from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []

# TODO: Challenge 4 jon


@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    return render_template('add.html')


# In case of a simple html form create a new route for recieving
@app.route("/recieve", methods=["POST"])
def recieve():
    # Get form data with request.form['html input's name attribute']
    all_books.append({"title": request.form['title'], "author": request.form['author'],  "rating": request.form['rating']})
    # A route must return a html, so we call the function that has this form in order not to change webpage
    return add()


if __name__ == "__main__":
    app.run(debug=True)

