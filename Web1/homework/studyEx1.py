from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/about-me")
def about_me():
    return "I am not human being. Just a hollow ghost passing by."

@app.route("/school")
def shcool():
    return redirect("http://techkids.vn",code = 302)



if __name__ == "__main__":
    app.run(debug = True)