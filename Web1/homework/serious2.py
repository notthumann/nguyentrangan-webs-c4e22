from flask import Flask,jsonify
app = Flask(__name__)

Users = {
	"nothuman" :{
        "name":"No Name",
        "age":0,
        "gender":"Male",
        "hobbies":"coding",
    },
    "annguyen" : {
        "name":"Nguyen Trang An",
        "age":22,
        "gender":"Male",
        "hobbies":"coding, movies",
    },       
}

@app.route("/user/<username>")
def user(username):
    if username in Users:
        return jsonify(Users[username])
    else:
        return "User not found"


if __name__ == '__main__':
  app.run(debug=True)