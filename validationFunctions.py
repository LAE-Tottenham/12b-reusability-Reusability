import requests

#Used in Task 1
def floatValidator(triangle):
    valid=False
    while valid==False:
        try:
            re_validate=True
            variable=float(input("Please input your triangle's " +triangle))
        except ValueError:
            re_validate=False
            print("Error. Please enter valid data type.")
        if re_validate==True:
            valid=True
    return variable

#Used in Task 2
def postcodeValidation():
    valid=False
    while valid==False:
        try:
            valid=True
            postcode_raw = input("\nSo, what's your postcode? ")
            postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode_raw}").json()

            area = postcode_resp['result']['admin_ward']
            longitude = postcode_resp['result']['longitude']
            latitude = postcode_resp['result']['latitude']
        except KeyError:
            valid=False
            print("Error. Please enter a valid postcode.")
    print(f"Nice! so you live in {area}.\n")
    return area, longitude, latitude
