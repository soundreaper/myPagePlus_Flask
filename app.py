from flask import Flask, render_template, url_for, request
import requests

app = Flask(__name__)

key = "ad958ab12b22f3901be8a6cdb93beec3"
okey = "pk.eyJ1Ijoib21hcnNzNjIiLCJhIjoiY2s3YXJsdGh4MG13ODNlcXJhY3l1NnMybiJ9.xmKZ0Yt2_b8evLDsrQcTqQ"


@app.route('/')
def index():
    """Index page of the application"""
    return render_template('index.html')

@app.route('/login')
def login():
    """Page for logging in"""
    return render_template('login.html')

@app.route('/register')
def register():
    """Page for registering"""
    return render_template('register.html')

@app.route("/weather")
def weather():
    location = request.args.get("address")
    coords = geocode(location)

    req = requests.get("https://api.darksky.net/forecast/"+ okey + "/"+ coords)

    reqJson = req.json()

    weather = {
        "temp": reqJson["currently"]["temperature"],
        "humidity": reqJson["currently"]["humidity"],
        "wind": reqJson["currently"]["windSpeed"],
        "summary": reqJson["currently"]["summary"],
        "high": reqJson["daily"]["temperatureHigh"],
        "low": reqJson["daily"]["temperatureLow"]
    }
    message = f"It is currently {weather['temp']} with a high of {weather['high']} and a low of {weather['low']}. "

    return render_template("index.html", weather=weather)


def geocode(location):
    url = 'https://api.mapbox.com/geocoding/v5/mapbox.places/'+ location +'.json?access_token=' + key + '&autocomplete=true'

    res = requests.get(url)
    latitude, longitude = res.json()["features"][0]["geometry"]["coordinates"]

    return str(latitude + ',' + longitude)

if __name__ == '__main__':
    app.run(debug=True)