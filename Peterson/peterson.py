from threading import Thread

flag=[False,False]#Creat a flag list whit default False value for each thread.
turn=0#Creat Turn variable whit default 0 value.
counter=0#Creat a variable as shared counter.

#define increament function as threads's targets:
def increment(txt,I,J,inc):#(txt is thread IDname, I is thread ID,J is other thread ID and inc is the value for every thread increamenting to rich that.)
    global counter,flag,turn 
    for _ in range(inc):
        #Peterson entry  section:
        flag[I]=True
        turn=J
        while flag[J]==True and turn == J:
            pass
        #Critical section:
        print(txt + " entered>>")
        counter += 1
        print(txt+ ": " + str(counter))
        print(txt + " exited<<\n----------")
        #Exit section:
        flag[I]=False
n1=20
n2=30
#Define two thread to target increament function an give them arguments: 
T1=Thread(target=increment, args=("A",0,1,n1))
T2=Thread(target=increment, args=("B",1,0,n2))
#Starting threads:
T1.start()
T2.start()
T1.join()
T2.join()
#At the end printing the last counted number to compare it to the expected value.
print(f"Final counter value: {counter}\nExpected result: {n1+n2}\n")
