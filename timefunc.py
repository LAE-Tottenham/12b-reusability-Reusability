import time

def delay(num): 
    time.sleep(num)
 
def wait(): 
    for i in range(3): 
        delay(1)
        print("...")   
