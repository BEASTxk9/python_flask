# BEFORE YOU START RUN " python3 -m pip install flask " TO INSTALL THE FLASK FRAMEWORK

# Import module
from flask import Flask
from views import views

# initialize application of the app
app = Flask(__name__)

# call routes
app.register_blueprint(views, url_prefix="/")


# (DOING THIS WORKS HOWEVER IT MAKES THIS FILE LOOK CLUTTERED THEREFORE ALL ROUTES ARE PLACED INTO THE VIEW.PY FILE )
# website path
# @app.route("/")
# def home():
#     return "this is the home page"


# run website
if __name__ == '__main__':
    app.run(debug=True, port=8000)