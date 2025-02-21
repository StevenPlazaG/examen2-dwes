from flask import Flask, redirect, render_template, request
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        email = request.form.get("email")
        password = request.form.get("password")
        return redirect("profile.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        email = request.form.get("email")
        password = request.form.get("password")
        return redirect("login.html")

def error404(error):
    return "<h1>Error 404: Ha ocurrido un error encontrando esta ruta, intenta con otra</h1>"

if __name__ == "__main__":
    app.register_error_handler(404, error404)
    app.run(debug=True)