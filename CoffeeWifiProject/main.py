from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from flask_bootstrap import Bootstrap5
import pandas

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    url = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', choices=["✘", "☕" * 1, "☕" * 2, "☕" * 3, "☕" * 4, "☕" * 5], validators=[DataRequired()])
    wifi = SelectField('Wifi Strength', choices=["✘", "💪" * 1, "💪" * 2, "💪" * 3, "💪" * 4, "💪" * 5], validators=[DataRequired()])
    power = SelectField('Power Socket Avaliability', choices=["✘", "🔌" * 1, "🔌" * 2, "🔌" * 3, "🔌" * 4, "🔌" * 5], validators=[DataRequired()])
    submit = SubmitField('Submit')


# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# ---------------------------------------------------------------------------
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------
def read_csv_():
    with open("cafe-data.csv", encoding="UTF-8") as file:
        data = pandas.read_csv(file).to_dict()
    return data


def write_csv_(*args):
    to_write = ""
    for arg in args:
        to_write += str(arg)+","
    to_write = to_write.removesuffix(",")
    to_write += "\n"

    with open("cafe-data.csv", "a", encoding="UTF-8") as file:
        file.write(to_write)


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("SUBMIT")
        write_csv_(form.name.data, form.url.data, form.open.data, form.close.data, form.coffee.data, form.wifi.data, form.power.data)

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    data = read_csv_()
    return render_template('cafes.html', cafes=data)


if __name__ == '__main__':
    app.run(debug=True)
