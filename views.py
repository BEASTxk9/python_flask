# install module
from flask import Blueprint, render_template

# initialize blueprint
views = Blueprint(__name__, "views")

# create route to index.html page
@views.route("/")
def home():
    # name and age acts as data that can be called on the html file by using {{}}
    return render_template("index.html", name="Shane", age=20)

# create route
# @views.route("/")
# def home():
#     return "home page"

