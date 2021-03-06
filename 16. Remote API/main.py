from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    query = "Mechelen, BE"
    unit = "metric"  # use "imperial" for Fahrenheit
    api_key = "e171d18ad0939e123582cd29b9a42a2f"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}".format(query, unit, api_key)
    data = requests.get(url=url)  # GET request to the OpenWeatherMap API

    return render_template("index.html", data=data.json())

if __name__ == '__main__':
    app.run(debug=True)