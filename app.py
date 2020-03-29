from flask import Flask, render_template
import data

app = Flask(__name__)


@app.route('/')
def route_index():
    return render_template("index.html", departures=data.departures, data=data)


@app.route('/departure/<departure>')
def route_departure(departure):
    return render_template("departure.html", departures=data.departures, data=data, dep=departure)


@app.route('/tour/<id>')
def route_tour(id):
    return render_template("tour.html", id=id, tour=data.tours[int(id)], departures=data.departures)


if __name__ == '__main__':
    app.run()
