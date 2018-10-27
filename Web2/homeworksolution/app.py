from flask import Flask,render_template
app = Flask(__name__)
@app.route('/bmi/<float:weight>/<int:height>')
def bmi(weight, height):
    result = weight / ((height/100)**2)
    return render_template("bmi.html", bmi = result)
#server-side template rendering
#fb: client-site template rendering

if __name__ == '__main__':
  app.run(debug=True)