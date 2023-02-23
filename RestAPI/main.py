from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

API_KEY = "TheSecretApiKey"

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Café TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def random_coffee():
    random_cafe = random.choice(db.session.query(Cafe).all())
    return jsonify(random_cafe.to_dict())


@app.route("/all")
def all_coffee():
    cafes = db.session.query(Cafe).all()
    return jsonify([cafe.to_dict() for cafe in cafes])


@app.route("/search")
def search():
    loc = request.args.get("loc")
    cafes_at_loc = db.session.query(Cafe).filter_by(location=loc)
    if cafes_at_loc:
        return jsonify([cafe.to_dict() for cafe in cafes_at_loc])
    return jsonify({"error": {"Not Found": "Sorry, we don't have a cafe at this location."}}), 404


@app.route("/add", methods=["POST"])
def add():
    name = str(request.args.get("name"))
    map_url = str(request.args.get("map_url"))
    img_url = str(request.args.get("img_url"))
    location = str(request.args.get("location"))
    seats = str(request.args.get("seats"))
    has_toilet = bool(request.args.get("has_toilet"))
    has_wifi = bool(request.args.get("has_wifi"))
    has_sockets = bool(request.args.get("has_sockets"))
    can_take_calls = bool(request.args.get("can_take_calls"))
    coffee_price = str(request.args.get("coffee_price"))

    new_cafe = Cafe(
        name=name,
        map_url=map_url,
        img_url=img_url,
        location=location,
        seats=seats,
        has_toilet=has_toilet,
        has_wifi=has_wifi,
        has_sockets=has_sockets,
        can_take_calls=can_take_calls,
        coffee_price=coffee_price,
    )

    db.session.add(new_cafe)
    db.session.commit()

    return jsonify({"Response": {"Success": "Succesfully added the new cafe."}}), 200


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    selected_cafe = db.session.query(Cafe).get(cafe_id)

    if selected_cafe:
        selected_cafe.coffee_price = new_price
        db.session.commit()

        return jsonify({"success": "Successfully updated the price."}), 200

    else:
        return jsonify({"error": {"Not Found": "Sorry a cafe with that id was not found in the database."}}), 404


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == API_KEY:
        cafe_to_delete = db.session.query(Cafe).get(cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify({"success": "Successfully deleted cafe."}), 200
        else:
            return jsonify({"error": {"Not Found": "Sorry a cafe with that id was not found in the database."}}), 404
    else:
        return jsonify({"error": "Incorrect api key"}), 403
    

# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
