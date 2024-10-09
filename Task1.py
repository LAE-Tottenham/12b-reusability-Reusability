# Help! My code is too messy :( Please help me organise it and extract out the duplications.

# Define your reusable functions here:

import triangleFunctions
import validationFunctions

# Make sure each function only does ONE thing!!!!!!!!!!!



###########################################

def weird_calculation():

    triangleEquations=""
    while triangleEquations.lower() not in ["pythagoras", "sine rule", "cosine rule", "soh", "cah", "toa"]:
        triangleEquations=input("Please choose one out of the following: 'pythagoras' 'sine rule' 'cosine rule' 'soh' 'cah' 'toa': ")


    #Triangle 1
    triangle_one=triangleFunctions.whichEquation(triangleEquations, 1, "", "")
    print("Found value: " +str(triangle_one))
    #Triangle 2
    triangle_two=triangleFunctions.whichEquation(triangleEquations, 2,"","")
    print("Found value for triangle 2: "+str(triangle_two))
    #Triangle 3
    triangle_three=triangleFunctions.whichEquation(triangleEquations, 3, triangle_one, triangle_two)
    print("Found value for triangle 3: ")
    return triangle_three

weird_answer = weird_calculation()
print(weird_answer)


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
# The inputs each have to be floats (or integers).
# 2. Validate the user's input based on your preconditions.
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
#It was useful as it meant I didn't have to constantly re-type out the same lines of code for each seperate opposite and adjacent. It also meant that when fixing any errors, I didn't have to individually hunt down and fix each seperate variable's error and instead could edit the single function.

# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
    #complete
# 2. In your new file add functions for SOH CAH TOA. Also for the sine and cosine rule.
    #complete
# 3. Let the user choose whether they would like to use Pythogras, SOH, CAH, TOA, sine or cosine rule. Then ask for the relavent information and return the result to them.
    #complete
# 4. Make sure all of your functions (except the main one) only do ONE thing or process.

# Extension:
# After you calculate the the result for the user. Use a library like Turtle to draw an approximation of their triangle for them.
# Hint: import the functions in drawing_functions.py and call them. See what happens. BTW check out the turtle docs for further info on how to use Turtle. 