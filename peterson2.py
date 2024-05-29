from threading import Thread
from time import sleep
from random import uniform,random

flag=[False]*10
turn=5
counter=0
def increment(txt,I,J):
    global counter,flag,turn
    for x in range(10):
        flag[I]=True
        turn=J
        while flag[J]==True and turn==J:
            pass
        counter += 1
        #sleep(random()/100)
        print(txt + str(counter))
        print('-----------------------------------------')
        sleep(3)
        flag[I]=False

T0=Thread(target=increment,args=("A: ",0,1,),daemon=True)
T1=Thread(target=increment,args=("B: ",1,2,),daemon=True)
T2=Thread(target=increment,args=("C: ",2,3,),daemon=True)
T3=Thread(target=increment,args=("D: ",3,4,),daemon=True)
T4=Thread(target=increment,args=("E: ",4,5,),daemon=True)
T5=Thread(target=increment,args=("F: ",5,6,),daemon=True)
T6=Thread(target=increment,args=("G: ",6,7,),daemon=True)
T7=Thread(target=increment,args=("H: ",7,8,),daemon=True)
T8=Thread(target=increment,args=("I: ",8,9,),daemon=True)
T9=Thread(target=increment,args=("J: ",9,0,),daemon=True)

T0.start()
T1.start()
T2.start()
T3.start()
T4.start()
T5.start()
T6.start()
T7.start()
T8.start()
T9.start()

T0.join()
T1.join()
T2.join()
T3.join()
T4.join()
T5.join()
T6.join()
T7.join()
T8.join()
T9.join()

print(f"Final counter value: " + str(counter))