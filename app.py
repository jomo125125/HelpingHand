from flask import Flask, request, jsonify
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash, redirect

global_email = ""
global_password = ""

app = Flask(__name__, template_folder="templates")


@app.route('/')
def homepage():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/register")
def register():
    return render_template("register.html")


app = Flask(__name__)

if __name__ == '__main__':
    app.run()


def index(): return 'Hello, World!'


@app.route("/submit", methods=["POST"])
def submit():
    email = request.form["email"]
    password = request.form["password"]
    global_email = email
    global_password = password
    return jsonify(
        {
            "test": global_email,
            "status": 200,
            "response": "Submitted successfully",
            "email": email,
            "password": password,
        }
    )


app.add_url_rule('/', 'index', index)

if __name__ == '__main__':
    app.run(debug=True)
