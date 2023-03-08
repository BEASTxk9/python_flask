# install module
from flask import Blueprint, render_template, request, jsonify, redirect, url_for

# initialize blueprint
views = Blueprint(__name__, "views")

# 1. _____________
# create home route by returning a string
# @views.route("/")
# def home():
#     return "home page"

# 2. _____________
# create home route by rendering a template via the index.html file
@views.route("/")
# create function that is embedded to the route
def home():
    # name and age acts as data that can be called on the html file by using {{}}
    return render_template("index.html", name="Shane")

# 3. _____________
# create route
@views.route("/user_profile")
# create function that is embedded to the route
def user_profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)
# open this link " http://127.0.0.1:8000/user_profile?name=bob " and it will display " Hello, bob " on the page


# 4. _____________
# create route
@views.route("/profile")
# create function that is embedded to the route
def profile():
    args = request.args
    name = args.get('name')
    return render_template("profile.html", name=name)
# open this link " http://127.0.0.1:8000/profile?name=bob " and it will display " Hello, bob " on the page

# 5. _____________
# create route to return json
@views.route("/json")
# create function that is embedded to the route
def get_json():
    return jsonify({'name':'shane', 'coolness':10})

# 6. _____________
# create route get json
@views.route("/data")
# create function that is embedded to the route
def get_data():
    data = request.json
    return jsonify(data)

# 7. _____________
# create redirect route
@views.route("/go-to-home")
# create function that is embedded to the route
def go_to_home():
    return redirect(url_for("views.home"))
