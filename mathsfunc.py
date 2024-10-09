import math

def hyp(opp, adj): 
    return math.sqrt(opp**2 + adj**2)

def len(type): 
    len = input("Enter your triangle's " + type + " side length: ")
    while len.isdigit() == False or int(len) <= 0: 
        len = input("You must enter a positive number as your triangle's " + type + " length: ")
    return float(len)

def soh(opp, angle): 
    return round(opp / math.sin(angle), 5)

def cah(adj, angle): 
    return round(adj / math.cos(angle), 5)

def toa(opp, adj):
    return math.atan(opp/adj)

def sineRule(side1, angle1, angle2):
    return round((side1 / math.sin(angle1)) * math.sin(angle2), 5)

def cosineRule(sideB, sideC, angleA): 
    return round(math.sqrt((sideB**2) + (sideC**2) - (2*sideB*sideC*math.cos(angleA))), 5)

def angle(): 
    angle = input("Please enter the size of the angle in degrees: ")
    return math.radians(float(angle))