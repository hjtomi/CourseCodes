from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def page_home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def recieve_data():
    return page_login_success(request.form["username"], request.form["password"])


@app.route("/loginsuccess")
def page_login_success(username, password):
    return f"<h1>Welcome {username}, with password {password}!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
