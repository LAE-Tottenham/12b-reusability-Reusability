from pyfiglet import Figlet
import os, requests, time

# Help! I'm trying to make this cool bot but my code is too messy :( Please help me organise it into reusable components.

# Define your reusable functions here:
import Task2Functions
import validationFunctions

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
    
    Task2Functions.genderGuesser()
    
    gender_correct = input("Am I right? :) (Y/n)")
    if gender_correct.lower() in ["", "yes", "y", "ye"]:
        print("Wooooooh! Computer 1, Human 0.")
    else:
        print("Ahhhh, sorry! :(")

    area, longitude, latitude=validationFunctions.postcodeValidation()

    print("Let me just check the weather there today...\n")
    
    Task2Functions.pause(3)
    
    input("\nWould you like a cat fact while you wait? ")

    #Further Task 3
    catFact=input("Too bad. You're not getting one. >:( ")
    time.sleep(3)

    if catFact.lower()=="please":
        print("Fine...")
        joke_resp = requests.get("https://catfact.ninja/fact").json()
        joke = joke_resp['fact']
    
        Task2Functions.factPrinter(joke)

    print("\nNow, back to getting the weather...")

    Task2Functions.pause(3)

    Task2Functions.weatherMachine(area, longitude, latitude)

weird_weather_bot()


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
    #The input postcode has to be a real postcode.
# 2. Validate the user's input based on your preconditions.
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
    #It makes the code much easier to read since the titles of functions (such as genderGuesser) has taken the place of longer chunks of coding, making it much simpler to understand what a piece of code does. It also reduces the amount of coding overall, as variables such as the area, longitude and latitude were able to be taken in just one line of code rather than requiring a separate line for each variable. It also made editing each section more convenient since I could edit and test each function without having to worry about the rest of the initial code.

# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. Make sure all of your functions (except the main one) only do ONE thing or process.
# 3. Add your own twist to the code.

# Extension:
# Add the following apis as reusable components and use them in your code:
# https://www.exchangerate-api.com/docs/overview
