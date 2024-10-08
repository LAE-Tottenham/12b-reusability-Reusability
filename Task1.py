# Help! My code is too messy :( Please help me organise it and extract out the duplications.

# Define your reusable functions here:
# Make sure each function only does ONE thing!!!!!!!!!!!

import mathsfunc

###########################################

def weird_calculation():
    # get the length and width of the first triangle from the user
    opp1 = mathsfunc.sideinput("first", "opposite")
    adj1 = mathsfunc.sideinput("first", "adjacent")

    # work out the hyp
    hyp1 = mathsfunc.pythagorus(opp1, adj1)

    # get the length and width of the second triangle from the user
    opp2 = mathsfunc.sideinput("second", "opposite")
    adj2 = mathsfunc.sideinput("second", "adjacent")
    
    # work out the hyp
    hyp2 = mathsfunc.pythagorus(opp2, adj2)

    # create a third triangle with the hyp1 as the opp and hyp2 as the adj
    hyp3 = mathsfunc.pythagorus(hyp1,hyp2)
    return hyp3

weird_answer = weird_calculation()
print(weird_answer)


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
# 2. Validate the user's input based on your preconditions.
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.

# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. In your new file add functions for SOH CAH TOA. Also for the sine and cosine rule.
# 3. Let the user choose whether they would like to use Pythogras, SOH, CAH, TOA, sine or cosine rule. Then ask for the relavent information and return the result to them.
# 4. Make sure all of your functions (except the main one) only do ONE thing or process.

# Extension:
# After you calculate the the result for the user. Use a library like Turtle to draw an approximation of their triangle for them.
# Hint: import the functions in drawing_functions.py and call them. See what happens. BTW check out the turtle docs for further info on how to use Turtle. 
