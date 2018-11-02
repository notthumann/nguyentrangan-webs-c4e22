from flask import Flask,render_template, request
import mlab
from poll import Poll
from random import choice

app = Flask(__name__)
mlab.connect()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/polls")
def polls():
  #1 Read all polls
  poll_list = Poll.objects()
  # for p in poll_list:
  #   print(p.question)

  #2. Render all polls
  return render_template("polls.html", polls = poll_list)

@app.route("/polls/<poll_code>")
def poll(poll_code):
  #1 Get pool
  poll_list = Poll.objects(code = poll_code)
  poll = poll_list[0]
  # print(poll.question)
  # print(poll.options)
  # object(yob__lt=1990)
  #2 Render
  return render_template("poll.html", p = poll)

@app.route("/new_poll", methods = ['GET','POST'])
def new_poll():
  if request.method == "GET":
    return render_template("new_poll.html")
  elif request.method == "POST":
    #1.Unpack data
    form = request.form
    question = form["question"]
    options = []
    for k,v in form.items():
      if k != "question":
        options.append(v)
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    code = ""
    for _ in range(6):
        code += choice(alphabet)
    p = Poll(question = question, options=options, code = code)
    p.save()
    return "Gotcha"

if __name__ == '__main__':
  app.run(debug=True)