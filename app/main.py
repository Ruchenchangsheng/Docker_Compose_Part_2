from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)
API_KEY = os.getenv("58d10a9101aac36473b919102c658c06")


@app.route("/weather")
def get_weather():
    lat = 55.75  # Moscow
    lon = 37.61
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    return jsonify({
        "temperature": data["current"]["temp"],
        "description": data["current"]["weather"][0]["description"],
        "humidity": data["current"]["humidity"]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
