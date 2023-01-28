from flask import Flask
import random

random_number = random.randint(1, 9)

app = Flask(__name__)


@app.route("/")
def main_page():
    return '<h1>Guess a number between 0 and 10</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:num>")
def guess(num):
    if num == random_number:
        return f'<h1>Wow, you guessed it!</h1>' \
               f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif num < random_number:
        return f'<h1>Too low!</h1>' \
               f'<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return f'<h1>Too high!</h1>' \
               f'<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
