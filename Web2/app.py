from flask import Flask,render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/new_poll", methods = ['GET','POST'])
def new_poll():
  if request.method == "GET":
    return render_template("new_poll.html")
  elif request.method == "POST":
    #1.Unpack data
    form = request.form
    question = form["question"]
    option = []
    for k,v in form.items():
      if k != "question":
        option.append(v)
    return "Gotcha"

if __name__ == '__main__':
  app.run(debug=True)