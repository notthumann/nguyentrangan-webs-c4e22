# setup flask server
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Welcome to C4E Web Module, enjoy"


@app.route("/quan")
def hello_quan():
    return "Hello Quan"

@app.route("/praise/linh")
def praise_linh():
    return "Linh is awesome"

@app.route("/praise/<name>")
def praise(name):
    return name + " is awesome"

@app.route("/add/<int:x>/<int:y>")
def add(x,y):
    r = int(x) + int(y)
    return str(r)

@app.route("/question")
def show_question():
    return render_template("question.html")



if __name__ == "__main__":
    app.run(debug = True)