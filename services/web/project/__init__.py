from os import getenv
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

# set secret key
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

admin = Admin(app, name='example_app', template_mode='bootstrap3')

class Child(db.Model):
    __tablename__ = "child"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __init__(self, user):
        self.username = username


class Parent(db.Model):
    __tablename__ = "parent"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    children = db.Column('Child', backref='parent')

    def __init__(self, user):
        self.username = username


# Add administrative views here
admin.add_view(ModelView(Child, db.session))
admin.add_view(ModelView(Parent, db.session))

@app.route("/")
def hello_world():
    return jsonify(hello="world")

