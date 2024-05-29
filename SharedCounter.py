from threading import Thread
from time import sleep
from random import uniform,random


counter=0
def increment(txt):
    global counter 
    
    for x in range(100):
        counter += 1
        sleep(random()/100)
        print(txt + str(counter))


T1=Thread(target=increment, args=("A: ",), daemon=True)
T2=Thread(target=increment, args=("B: ",), daemon=True)
T3=Thread(target=increment, args=("C: ",), daemon=True)
T4=Thread(target=increment, args=("D: ",), daemon=True)
T1.start()
T2.start()
T3.start()
T4.start()
T1.join()
T2.join()
T3.join()
T4.join()
print(f"Final counter value: " + str(counter))