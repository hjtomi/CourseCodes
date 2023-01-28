from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def nested_function():
        return f"<b>{function()}</b>"

    return nested_function


def make_italic(function):
    def nested_function():
        return f"<em>{function()}</em>"

    return nested_function


def make_underlined(function):
    def nested_function():
        return f"<u>{function()}</u>"

    return nested_function


@app.route('/')
def hello_world():
    return '<h1>This is my website!</h1>' \
           '<p>I love my website this much:</p>' \
           '<img src="https://media3.giphy.com/media/26FLdmIp6wJr91JAI/giphy.gif?cid=ecf05e47cfg43plyfbp45ept38kili6ltxbw42xjlsbxlbzj&rid=giphy.gif&ct=g">' \
           '<p>As you can see I am a really big fan of my website</p>'


@app.route('/bye')
@make_bold
@make_italic
@make_underlined
def bye():
    return "Bye!"


@app.route('/user/<name>')
def greet(name):
    return f'Hello {name}'


if __name__ == "__main__":
    app.run(debug=True)
