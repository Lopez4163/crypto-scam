from cgitb import html
from flask import Blueprint, render_template
from .dict import coin_dict


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", coin_dict=coin_dict)
    