from flask import Flask, render_template
app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight,height):
    h = height / 100 #convert to m
    bmi = weight / (h * h)
    if bmi < 16:
        return render_template("severlyunderweight.html")
    elif 16 < bmi < 18.5 :
        return render_template("underweight.html")
    elif 18.5 < bmi < 25 :
        return render_template("normal.html")
    elif 25 < bmi < 30 :
        return  render_template("overweight.html")
    else:
        return  render_template("obese.html")

if __name__ == '__main__':
    app.run(debug=True)