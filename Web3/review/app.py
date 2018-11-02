from flask import Flask,render_template, request
import mlab
from registration import Users

app = Flask(__name__)
mlab.connect()

@app.route("/", methods = ["POST","GET"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    elif request.method == "POST":
        form = request.form
        firstname = form["First name"]
        lastname = form["Last name"]
        email = form["Email"]
        yob = form["Yob"]
        gender = form["gender"]
        city = form["City"]
        u = Users(firstname = firstname, lastname = lastname, email = email, yob = yob, gender = gender, city = city)
        u.save()
        return "OK"
        
if __name__ == '__main__':
  app.run(debug=True)