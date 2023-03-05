from flask import Flask, render_template, url_for, request, redirect, flash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "ikjuldxkiljdfxcijkulmdesfjuhkm"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/")
def home():
    return "<a href='http://127.0.0.1:5000/login'>raklattyintassz</a>"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_user(User.query.get(1))
        flash("logged in user.")

        return redirect(url_for("home"))

    return render_template('index.html')


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/secrets")
@login_required
def secrets():
    return "secret page"


if __name__ == "__main__":
    app.run(debug=True)
