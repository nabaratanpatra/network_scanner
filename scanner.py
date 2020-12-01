import socket
from datetime import datetime
import threading
from queue import Queue

#this will prevent duplicate inputs from shared variables
print_lock = threading.Lock()


#Enter host To scan
host = input ("enter the HOST IP address to scan :" )
ip = socket.gethostbyname(host) #trabnslate a host to ipv4 address format

#these theree lines are just for look
print("-" * 80)
print("PLease wait while we scan the host---->", ip)
print("-" * 80)

#starting time 
t1 = datetime.now()

#now write the code for port scanning
def scan(port):
    try:
        for port in range(1,100):
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #it cretaes the sock stream
            result = sock.connect((ip,port))
            if result == 0:
                #if a socket is listening it will print our the port number
                print("\n Port %d is OPEN --------> " %(port))
                sock.close()
            else:
                print("\n Port %d is close :-(" %(port))
    except:
        pass

#create threader function
def threader():
    while True:
        worker = q.get() #get worker from the queue
        scan(worker) #scanis a function & is responsible tu run jobs with available workrs in queue
        q.task_done() #complete with the job 

#create a queue by
q = Queue()

#writing for loop for the number of threa to allow
for x in range(60):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1,100):
    q.put(worker)

#thread will join after thread termination
q.join()

#calculate end of exec time
t2 = datetime.now()
#calculate the difference 
total = t2 -t1
#print the difference
print("Total scanning time: ", total)

#increase number of threads to increrase the speed of detection
#change the worker range to specify the range within which you want to scan targets 