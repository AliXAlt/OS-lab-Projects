import threading
from threading import Thread
import time

done = False
counter = 1

def workerA(dly,txt):
    global counter
    while not done:
        counter = counter+1
        time.sleep(dly)
        print( txt + str(counter) )  
def workerB(dly,txt):
    global counter
    while not done:
        counter = counter+1
        time.sleep(dly)
        print( txt + str(counter) )

TWB= Thread(target=workerA, args=(0.03 ,"Worker A: ",) , daemon=True)
TWA= Thread(target=workerB, args=(0.07 ,"Worker B: ",) , daemon=True)
TWA.start()
TWB.start()

input()
done = True
