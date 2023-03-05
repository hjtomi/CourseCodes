import werkzeug.security
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home():
    user_active = False
    if current_user.is_authenticated:
        user_active = True

    return render_template("index.html", logged_in=user_active)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if User.query.filter_by(email=request.form["email"]).first():
            flash("Account already exists with this email, log in instead!")
            return redirect(url_for('login'))

        new_user = User()
        new_user.email = request.form["email"]
        new_user.password = generate_password_hash(password=request.form["password"],
                                                   method="pbkdf2:sha256",
                                                   salt_length=8
                                                   )
        new_user.name = request.form["name"]
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('secrets', name=request.form["name"]))

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = db.session.query(User).filter_by(email=request.form.get('email')).first()
        if user:

            if check_password_hash(user.password, password=request.form.get('password')):

                login_user(user)

                return redirect(url_for('secrets', name=user.name))

            else:
                flash("Incorrect password")

        else:
            flash("No user with this email")

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    name = request.args.get("name")
    return render_template("secrets.html", name=name)


@app.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for("home"))


@app.route('/download')
def download():
    return send_from_directory(directory=app.static_folder, path="files/cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
