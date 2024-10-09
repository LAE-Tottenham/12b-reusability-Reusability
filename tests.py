import requests, time

input("\nWould you like a cat fact while you wait? ")
print("Doesn't matter what you think, I'm going to give you one anyway :)")
time.sleep(3)
joke_resp = requests.get("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/?number=1").json()
joke = joke_resp['fact']
print("\n###########################")
print("CAT FACT:")
print(f"\n{joke}\n")
print("So interesting isn't it!")
print("###########################")