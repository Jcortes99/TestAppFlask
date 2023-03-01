from flask import Flask, render_template, Response
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run()