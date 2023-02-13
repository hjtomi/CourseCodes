from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = "123456789"

Bootstrap5(app)


class LoginForm(FlaskForm):
    email = StringField(label='Email: ', validators=(DataRequired(), Email()))
    password = PasswordField(label="Password: ", validators=(DataRequired(), Length(min=6, max=20)))
    submit = SubmitField(label='Log in')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        correct_email = login_form.email.data == "admin@email.com"
        correct_password = login_form.password.data == "12345678"

        if correct_email and correct_password:
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
