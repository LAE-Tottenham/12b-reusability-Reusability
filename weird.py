import math

def sideinput(nth, sidetype):
    inp = input("Enter your " + nth +" triangle's " + "side length:");
    try:
        return float(inp)
    except:
        return sideinput(nth, sidetype)

def Pythogras(opp, adj):
    hyp = math.sqrt(opp**2 + adj**2)
    return hyp