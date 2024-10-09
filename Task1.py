# Help! My code is too messy :( Please help me organise it and extract out the duplications.

# Define your reusable functions here:
import mathsfunc





# Make sure each function only does ONE thing!!!!!!!!!!!



###########################################


def weird_calculation():
    
    process = input("Would you like to use pythagoras, soh, cah, toa, sine rule or cosine rule? ").lower()
    
    if process == "pythagoras": 
        # get the length and width of the first triangle from the user
        opp1 = mathsfunc.len("opposite")
        adj1 = mathsfunc.len("adjacent")
        # work out the hyp
        hyp1 = mathsfunc.hyp(opp1, adj1)

    elif process == "soh": 
        opp1 = mathsfunc.len("opposite")
        angle = mathsfunc.angle()
        hyp1 = mathsfunc.soh(opp1, angle)


    elif process == "cah": 
        adj1 = mathsfunc.len("adjacent")
        angle = mathsfunc.angle()
        hyp1 = mathsfunc.cah(adj1, angle)   

    elif process == "toa": 
        opp1 = mathsfunc.len("opposite")
        adj1 = mathsfunc.len("adjacent")
        angle = mathsfunc.toa(opp1, adj1)
        hyp1 = mathsfunc.soh(opp1, angle)
        
    elif process == "sine rule": 
        side1 = mathsfunc.len("opposite")
        angle1 = mathsfunc.angle()
        angle2 = mathsfunc.angle()
        hyp1 = mathsfunc.sineRule(side1, angle1, angle2)

    elif process == "cosine rule": 
        side1 = mathsfunc.len("opposite") 
        side2 = mathsfunc.len("adjacent")
        angle1 = mathsfunc.angle()
        hyp1 = mathsfunc.cosineRule(side1, side2, angle1)
    

    process = input("Would you like to use pythagoras, soh, cah, toa, sine rule or cosine rule? ")

    if process == "pythagoras": 
        # get the length and width of the first triangle from the user
        opp1 = mathsfunc.len("opposite")
        adj1 = mathsfunc.len("adjacent")
        # work out the hyp
        hyp2 = mathsfunc.hyp(opp1, adj1)

    elif process == "soh": 
        opp1 = mathsfunc.len("opposite")
        angle = mathsfunc.angle()
        hyp2 = mathsfunc.soh(opp1, angle)


    elif process == "cah": 
        adj1 = mathsfunc.len("adjacent")
        angle = mathsfunc.angle()
        hyp2 = mathsfunc.cah(adj1, angle)   

    elif process == "toa": 
        opp1 = mathsfunc.len("opposite")
        adj1 = mathsfunc.len("adjacent")
        angle = mathsfunc.toa(opp1, adj1)
        hyp2 = mathsfunc.soh(opp1, angle)
        
    elif process == "sine rule": 
        side1 = mathsfunc.len("opposite")
        angle1 = mathsfunc.angle()
        angle2 = mathsfunc.angle()
        hyp2 = mathsfunc.sineRule(side1, angle1, angle2)

    elif process == "cosine rule": 
        side1 = mathsfunc.len("opposite") 
        side2 = mathsfunc.len("adjacent")
        angle1 = mathsfunc.angle()
        hyp2 = mathsfunc.cosineRule(side1, side2, angle1)

    hyp3 = round(mathsfunc.hyp(hyp1, hyp2), 5)
    return hyp3

weird_answer = weird_calculation()
print(weird_answer)


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
    # the preconditions for the code not to break is that the value enter must be a positive number.

# 2. Validate the user's input based on your preconditions.

# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
    #One reason to use reusable components is because many calculations repeated to calculate the hypotenuse of each triangle, therefor using one function to calculate the
    # hypotenuse for each triangle requires less code and is simpler.
    # Another reason for using reusable components is that it allows for the collection of inputs faster, as the same code is repeated using a function to collect the input of 
    # the side length of the triangle from the user. 


# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.

# 2. In your new file add functions for SOH CAH TOA. Also for the sine and cosine rule.

# 3. Let the user choose whether they would like to use Pythogras, SOH, CAH, TOA, sine or cosine rule. Then ask for the relavent information and return the result to them.

# 4. Make sure all of your functions (except the main one) only do ONE thing or process.

# Extension:
# After you calculate the the result for the user. Use a library like Turtle to draw an approximation of their triangle for them.
# Hint: import the functions in drawing_functions.py and call them. See what happens. BTW check out the turtle docs for further info on how to use Turtle. 
