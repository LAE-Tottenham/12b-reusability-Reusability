
import requests
from pyfiglet import Figlet
import os, time

# Help! I'm trying to make this cool bot but my code is too messy :( Please help me organise it into reusable components.

# Define your reusable functions here:
import timefunc

# Make sure each function only does ONE thing!!!!!!!!!!!

def guess_gender(name):
    gender_resp = requests.get(f"https://api.genderize.io/?name={name}").json()
    gender = gender_resp["gender"]
    prob_percent = gender_resp["probability"] * 100
    return [gender, prob_percent]

###########################################

def weird_weather_bot():
    
    f = Figlet(font="slant")
    print(f.renderText("HEY!"))

    print("Welcome to the weird weather bot :)")
    print("-----------------------------------\n")
    name = input("May I take your first name please? ")
    while name.isalpha() == False: 
        name = input("Please enter a name that consists of only letters: ")
    gender_result = guess_gender(name)
    gender = gender_result[0]
    prob_percent = gender_result[1]
    print(f"\nHmmm, I'm {prob_percent}% sure you are a {gender}.")
    
    gender_correct = input("Am I right? :) (Y/n)")
    if gender_correct.lower() in ["", "yes", "y", "ye"]:
        print("Wooooooh! Computer 1, Human 0.")
    else:
        print("Ahhhh, sorry! :(")

    postcode_raw = input("\nSo, what's your postcode? ")
    postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode_raw}").json()


    area = postcode_resp['result']['admin_ward']
    longitude = postcode_resp['result']['longitude']
    latitude = postcode_resp['result']['latitude']
    print(f"Nice! so you live in {area}.\n")

    print("Let me just check the weather there today...\n")
    
    timefunc.wait()
    
    answer = input("\nWould you like a cat fact while you wait? ").lower()
    
    if answer == "yes" or answer == "y" or answer == "ye" or answer == "yeah":
        print("Yay, finally someone who also loves cats!!")
    else: 
        print("Doesn't matter what you think, I'm going to give you one anyway :)")
    
    timefunc.delay(3)
    joke_resp = requests.get("https://catfact.ninja/fact").json()
    joke = joke_resp['fact']
    print("\n###########################")
    print("CAT FACT:")
    print(f"\n{joke}\n")
    print("So interesting isn't it!")
    print("###########################")

    print("\nWaiting 5 seconds for you to read the fact...")
    timefunc.delay(5)
    print("\nNow, back to getting the weather...")

    timefunc.wait()
    weather_resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=4d30afa58f6f935d861edecad3639cda").json()
    # print(weather_resp)
    weather_kelvin = weather_resp["main"]["temp"]
    # convert to degrees
    weather_degrees = int(weather_kelvin - 273.15)
    main_weather_desc = weather_resp["weather"][0]["main"]
    second_weather_desc = weather_resp["weather"][0]["description"]
    print(f"\nThe weather in {area}:\n")
    print(str(weather_degrees) + "℃")
    print(f"{main_weather_desc} - {second_weather_desc}")
    print("\nThank you! Bye.")

weird_weather_bot()


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
    
    #one precondition is that the name needs to be valid, otherwise the code will return that the "probability of being a None is 0.0%"

# 2. Validate the user's input based on your preconditions.

# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
    # one reason it was useful to use reusable components is because this particular code is relatively complicated, so the reusable components
    # simplify the code and make it easier to understand and read. 
    # another reason that it was useful to use reusable components is because it makes it easier to make adjustments to the code instead of having
    # to rewrite an entire section of code multiple times.

# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.

# 2. Make sure all of your functions (except the main one) only do ONE thing or process.

# 3. Add your own twist to the code.
    #added an extra line if the user answers "yes" to if they want a cat fact.


# Extension:
# Add the following apis as reusable components and use them in your code:
# https://www.exchangerate-api.com/docs/overview
