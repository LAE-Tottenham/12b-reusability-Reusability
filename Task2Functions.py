import time, requests

#Had to move this here so it could be used in genderGuesser
def guess_gender(name):
    gender_resp = requests.get(f"https://api.genderize.io/?name={name}").json()
    gender = gender_resp["gender"]
    prob_percent = gender_resp["probability"] * 100
    return [gender, prob_percent]

def genderGuesser():
    name = input("May I take your first name please? ")
    gender_result =guess_gender(name)
    gender = gender_result[0]
    prob_percent = gender_result[1]
    print(f"\nHmmm, I'm {prob_percent}% sure you are a {gender}.")

def pause(seconds):
    for i in range (seconds):
        time.sleep(1)
        print("...")

def factPrinter(joke):
    print("\n###########################")
    print("CAT FACT:")
    print(f"\n{joke}\n")
    print("So interesting isn't it!")
    print("###########################")
    print("\nWaiting 5 seconds for you to read the fact...")
    time.sleep(5)

def weatherMachine(area, longitude, latitude):
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