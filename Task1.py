# Help! My code is too messy :( Please help me organise it and extract out the duplications.

# Define your reusable functions here:
# Make sure each function only does ONE thing!!!!!!!!!!!



###########################################
import math
def weird_calculation(opp1,adj1,opp2,abj2):
    hyp1 = math.sqrt(opp1**2 + adj1**2)
    hyp2 = math.sqrt(opp2**2 + adj2**2)
    opp3 = hyp1
    adj3 = hyp2
    hyp3 = math.sqrt(opp3**2 + adj3**2)
    return hyp3

while True:
    try:
        opp1 = float(input("Enter your first triangle's opposite side length: "))
    except ValueError:
        print("Not accepted, try again")
    else:
        break

while True:
    try:
        adj1 = float(input("Enter your first triangle's adjacent side length: "))
    except ValueError:
        print("Not accepted, try again")
    else:
        break

while True:
    try:
        opp2 = float(input("Enter your second triangle's opposite side length: "))
    except ValueError:
        print("Not accepted, try again")
    else:
        break

while True:
    try:
        adj2 = float(input("Enter your second triangle's adjacent side length: "))
    except ValueError:
        print("Not accepted, try again")
    else:
        break
        
 
print(weird_calculation(opp1,adj1,opp1,adj2))


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
    # the input for the variable need to be a number, can't be empty and can't be negative
# 2. Validate the user's input based on your preconditions.
    #Done 
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
    #Use define function helps to shorten codes, therefore easiler to look for where the mistake is.
    # We only need to write the define function once and when change the code, we only need to change it once.
# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. In your new file add functions for SOH CAH TOA. Also for the sine and cosine rule.
# 3. Let the user choose whether they would like to use Pythogras, SOH, CAH, TOA, sine or cosine rule. Then ask for the relavent information and return the result to them.
# 4. Make sure all of your functions (except the main one) only do ONE thing or process.

# Extension:
# After you calculate the the result for the user. Use a library like Turtle to draw an approximation of their triangle for them.
# Hint: import the functions in drawing_functions.py and call them. See what happens. BTW check out the turtle docs for further info on how to use Turtle. 
