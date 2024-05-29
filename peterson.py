from threading import Thread
from time import sleep
from random import random

flag=[False,False]#Creat a flag list whit default False value for each thread.
turn=0#Creat Turn variable whit default 0 value.
counter=0#Creat a variable as shared counter.

#define increament function as threads's targets:
def increment(txt,I,J,inc):#(txt is thread name, I is thread ID,J is other thread ID and inc is the value for every thread increamenting to rich that.)
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
