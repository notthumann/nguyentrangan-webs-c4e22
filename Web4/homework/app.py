from flask import Flask, render_template
import mlab
from rivers import River


app = Flask(__name__)
mlab.connect()


@app.route("/riversinafrica")
def river_in_africa():
    river_list = River.objects()
    # for r in river_list:
    #     print(r.name)
    return render_template("riversinafrica.html", rivers = river_list)

@app.route("/riverinsamericalt1000km")
def river_in_america_lt_1000_km():
    short_river_list = River.objects(length__lt=1000)
    for r in short_river_list:
        print(r.name)
    return render_template("riverinsamericalt1000km.html", short_rivers = short_river_list)
if __name__ == '__main__':
  app.run(debug=True)