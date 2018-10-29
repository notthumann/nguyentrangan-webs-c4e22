from flask import Flask,render_template, request
app = Flask(__name__)

@app.route("/", methods = ["POST","GET"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    elif request.method == "POST":
        form = request.form
        user = {}
        for k,v in form.items():
            user[k] = v
        print(user)
        return "OK"
        
if __name__ == '__main__':
  app.run(debug=True);.l,;.