from flask import Flask
app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight,height):
    h = height / 100 #convert to m
    bmi = weight / (h * h)
    if bmi < 16:
        return "Severly underweight"
    elif 16 < bmi < 18.5 :
        return "Underweight"
    elif 18.5 < bmi < 25 :
        return "Normal"
    elif 25 < bmi < 30 :
        return  "Overweight"
    else:
        return  "Obese"

if __name__ == '__main__':
    app.run(debug=True)