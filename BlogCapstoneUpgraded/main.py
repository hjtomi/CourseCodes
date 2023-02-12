from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
data = response.json()

app = Flask(__name__)


@app.route("/")
def page_home():
    return render_template("index.html", posts=data)


@app.route("/posts/<int:id>")
def page_post(id):
    return render_template("post.html", post=data[id-1])


@app.route("/about")
def page_about():
    return render_template("about.html")


@app.route("/contact")
def page_contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
