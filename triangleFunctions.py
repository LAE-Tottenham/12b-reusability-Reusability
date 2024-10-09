#All used for Task 1
import math
import validationFunctions

def hypotenuse(hyp,opp,adj):
    if hyp!=3:
        opp=validationFunctions.floatValidator("opposite side length: ")
        adj=validationFunctions.floatValidator("adjacent side length: ")
    else:
        opp3=opp
        adj3=adj
    hypot=math.sqrt(opp**2+adj**2)
    return hypot

def soh():
    hypot=validationFunctions.floatValidator("hypotenuse length: ")
    opp=validationFunctions.floatValidator("opposite side length: ")
    sine=math.degrees(math.asin(opp/hypot))
    return sine

def cah():
    hypot=validationFunctions.floatValidator("hypotenuse length: ")
    adj=validationFunctions.floatValidator("adjacent side length: ")
    cosine=math.degrees(math.acos(adj/hypot))

def toa():
    opp=validationFunctions.floatValidator("opposite side length: ")
    adj=validationFunctions.floatValidator("adjacent side length: ")
    tan=math.degrees(math.atan(opp/adj))

def sineRule():
    angle_or_side=""

    while (angle_or_side.lower()!="side") and (angle_or_side.lower()!="angle"):
        angle_or_side=input("Please select which of the options you are trying to find: 'side', 'angle': ")

    if angle_or_side.lower()=="side":
        knownSide=validationFunctions.floatValidator("known side length: ")
        opp_angle=validationFunctions.floatValidator("opposite angle (angle opposite the known side): ")
        needed_angle=validationFunctions.floatValidator("angle opposite the unknown side: ")
        missingAspect=((knownSide/math.sin(math.radians(opp_angle)))*math.sin(math.radians(needed_angle)))

    elif angle_or_side.lower()=="angle":
        knownAngle=validationFunctions.floatValidator("known angle length: ")
        opp_side=validationFunctions.floatValidator("known side that's opposite the known angle: ")
        needed_side=validationFunctions.floatValidator("known side length that is opposite the unknown angle: ")
        missingAspect=math.degrees(math.asin(((math.sin(math.radians(knownAngle))/opp_side)*needed_side)))

    return missingAspect

def cosineRule():
    knownSideB=validationFunctions.floatValidator("first known side length: ")
    knownSideC=validationFunctions.floatValidator("second known side length: ")
    knownAngle=validationFunctions.floatValidator("known angle which is opposite the unknown side: ")
    missingSide=math.sqrt(((knownSideB**2)+(knownSideC**2)-(2*(knownSideC*knownSideB*(math.cos(math.radians(knownAngle)))))))
    return missingSide

def whichEquation(choice, hyp, opp, adj):
    if choice.lower()=="soh":
        returnedAspect=soh()
    elif choice.lower()=="cah":
        returnedAspect=cah()
    elif choice.lower()=="toa":
        returnedAspect=toa()
    elif choice.lower()=="pythagoras":
        returnedAspect=hypotenuse(hyp, opp, adj)
    elif choice.lower()=="sine rule":
        returnedAspect=sineRule()
    elif choice.lower()=="cosine rule":
        returnedAspect=cosineRule()
    return returnedAspect