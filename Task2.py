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


# Reusable functions


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

# Main function that uses the reusable components

def weird_weather_bot():
    """Main function to execute the weather bot logic."""
    
    show_ascii_art("HEY!")
    print("Welcome to the weird weather bot :)")
    print("-----------------------------------\n")
    
    # Step 1: Ask for the user's name and guess their gender
    name = input("May I take your first name please? ")
    gender, prob_percent = guess_gender(name)
    print(f"\nHmmm, I'm {prob_percent}% sure you are a {gender}.")
    
    gender_correct = input("Am I right? :) (Y/n): ")
    if gender_correct.lower() in ["", "yes", "y", "ye"]:
        print("Wooooooh! Computer 1, Human 0.")
    else:
        print("Ahhhh, sorry! :(")

    # Step 2: Ask for the user's postcode and fetch info
    postcode = input("\nSo, what's your postcode? ")
    area, longitude, latitude = get_postcode_info(postcode)
    print(f"Nice! so you live in {area}.\n")

    # Step 3: Delay while fetching weather and provide a cat fact
    print("Let me just check the weather there today...\n")
    delay_with_dots(3)

    input("\nWould you like a cat fact while you wait? ")
    print("Doesn't matter what you think, I'm going to give you one anyway :)")
    time.sleep(3)

    # Step 4: Fetch and display the cat fact
    cat_fact = get_cat_fact()
    print("\n###########################")
    print("CAT FACT:")
    print(f"\n{cat_fact}\n")
    print("So interesting isn't it!")
    print("###########################")

    # Step 5: Display the weather
    print("\nWaiting 5 seconds for you to read the fact...")
    time.sleep(5)
    print("\nNow, back to getting the weather...")
    delay_with_dots(3)
    
    weather_degrees, main_desc, second_desc = get_weather(latitude, longitude)
    print(f"\nThe weather in {area}:\n")
    print(f"{weather_degrees}℃")
    print(f"{main_desc} - {second_desc}")
    
    print("\nThank you! Bye.")

# Run the bot
weird_weather_bot()


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break? 
#The get_weather function requires a valid OpenWeatherMap API key
# 2. Validate the user's input based on your preconditions.
#Ensure the name is not empty.
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise. It makes it so you don't have to type multiple times and you can save time.

# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. Make sure all of your functions (except the main one) only do ONE thing or process.
# 3. Add your own twist to the code.

# Extension:
# Add the following apis as reusable components and use them in your code:
# https://www.exchangerate-api.com/docs/overview
