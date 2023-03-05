from flask import Flask, render_template, request
import requests
import smtplib


my_email = "hegymegijakotamas@gmail.com"
password = "gnuahqrwabtmhaei"

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
data = response.json()

app = Flask(__name__)


@app.route("/")
def page_home():
    return render_template("index.html", posts=data)


@app.route("/posts/<int:iden>")
def page_post(iden):
    return render_template("post.html", post=data[iden-1])


@app.route("/about")
def page_about():
    return render_template("about.html")


@app.route("/contact")
def page_contact():
    return render_template("contact.html")


@app.route("/recieve", methods=["POST"])
def recieve_data():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            my_email,
            my_email,
            f"Subject:New Contact\n\nName: {name}\nEmail: {email}\nPhone number: {phone}\nMessage: {message}"
        )
    return recieve_success(name, email, phone, message)


@app.route("/recieve_success")
def recieve_success():
    return f"<h1>MESSAGE SENT SUCCESFULLY!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
