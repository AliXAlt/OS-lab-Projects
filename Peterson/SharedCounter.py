from threading import Thread

counter=0

def increment(txt):

    global counter     

    for x in range(100):

        print(txt + ">>entered.")
        counter += 1
        print(txt + str(counter))
        print(txt + "<<exited.\n----------")

T1=Thread(target=increment, args=("A: ",))
T2=Thread(target=increment, args=("B: ",))

T1.start()
T2.start()
T1.join()
T2.join()

print(f"Final counter value: {counter}")