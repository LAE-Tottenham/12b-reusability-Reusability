import requests
import time
from pyfiglet import Figlet

def provide_weather_advice(temp, main_desc):
    if temp > 30:
        return "It's boiling! Wear sunscreen!"
    elif temp < 10:
        return "Better bundle up, it's freezing out there!"
    else:
        return f"Seems like a {main_desc.lower()} day, enjoy it!"

def guess_gender(name):
    """Determines gender prediction based on the provided name."""
    gender_resp = requests.get(f"https://api.genderize.io/?name={name}").json()
    gender = gender_resp.get("gender", "unknown")
    prob_percent = gender_resp.get("probability", 0) * 100
    return gender, prob_percent

def get_postcode_info(postcode):
    """Fetches area, latitude, and longitude based on the postcode."""
    postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode}").json()
    result = postcode_resp.get('result', {})
    area = result.get('admin_ward', 'unknown')
    longitude = result.get('longitude', 0)
    latitude = result.get('latitude', 0)
    return area, longitude, latitude

def get_weather(latitude, longitude):
    """Fetches weather details using latitude and longitude."""
    weather_resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=YOUR_API_KEY").json()
    weather_kelvin = weather_resp.get("main", {}).get("temp", 273.15)
    weather_degrees = int(weather_kelvin - 273.15)  # Convert Kelvin to Celsius
    weather = weather_resp.get("weather", [{}])[0]
    main_weather_desc = weather.get("main", "Unknown")
    second_weather_desc = weather.get("description", "Unknown")
    return weather_degrees, main_weather_desc, second_weather_desc

def get_cat_fact():
    """Fetches a random cat fact."""
    joke_resp = requests.get("https://catfact.ninja/fact").json()
    return joke_resp.get('fact', 'No fact available.')

def show_ascii_art(text):
    """Displays ASCII art."""
    f = Figlet(font="slant")
    print(f.renderText(text))

def delay_with_dots(seconds):
    """Delays the program and prints dots for a given number of seconds."""
    for i in range(seconds):
        time.sleep(1)
        print("...")