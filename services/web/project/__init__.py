from os import getenv
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

# set secret key
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

admin = Admin(app, name='example_app', template_mode='bootstrap3')

class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    addresses = relationship("Address", back_populates="user")

class Address(db.Model):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates="addresses")


# Add administrative views here
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Address, db.session))

@app.route("/")
def hello_world():
    return jsonify(hello="world")

