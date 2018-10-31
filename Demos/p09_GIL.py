import time
import threading

def counter():
    max = 50000000
    while max > 0:
        max -= 1
    max = 0
    
thread1 = threading.Thread(target=counter)
thread2 = threading.Thread(target=counter)

start = time.time()
#counter()
thread1.start()
thread2.start()

thread1.join()
thread2.join()

end = time.time()
print ("The time taken is: ", end-start)
