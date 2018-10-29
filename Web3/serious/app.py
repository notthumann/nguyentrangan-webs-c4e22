from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/new_bike", methods = ["POST","GET"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    elif request.method == "POST":
        form = request.form
        new_bike = {}
        for k,v in form.items():
            new_bike[k] = v
        print(new_bike)
        print(form)
        return "OK"

if __name__ == '__main__':
    app.run(debug=True)