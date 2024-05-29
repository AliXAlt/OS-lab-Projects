from threading import Thread
from time import sleep
from random import random


flag=[False,False]
turn=0
counter=0

def increment(txt,I,J,inc):
    global counter,flag,turn 
    for _ in range(inc):
        #Peterson entry  section:
        flag[I]=True
        turn=J
        while flag[J]==True and turn == J:
            continue
        #Critical section:
        print(txt + ">>entered.")
        counter += 1
        print(txt + str(counter))
        print(txt + "<<exited.\n----------")
        #Exit section:
        flag[I]=False


T1=Thread(target=increment, args=("A: ",0,1,60))
T2=Thread(target=increment, args=("B: ",1,0,40))


T1.start()
T2.start()


T1.join()
T2.join()


print(f"Final counter value: {counter}")
