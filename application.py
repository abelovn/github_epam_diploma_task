from flask import Flask, render_template, url_for
import sys
application = Flask(__name__)






@application.route("/")
def index():
    return render_template("index.html")


@application.route("/about")
def about():
    return render_template("about.html")


@application.route("/user/<username>")
def show_user_page(username):
    return "Hello " + username.upper()


# Start local project
if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0')