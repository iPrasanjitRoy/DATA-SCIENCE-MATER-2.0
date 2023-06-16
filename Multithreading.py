import threading 
def TEST(id):
    print("PROGRAME START ", id) 

TEST(1000)

MyVariable = [threading.Thread(target=TEST, args=(i,)) for i in range(10)] 
for t in MyVariable:
    t.start()  

#02 ----------------> --------------------------------> -----------------> 
import threading 
import urllib.request

def file_downlaod(url , filname) : 
    urllib.request.urlretrieve(url,filname) 

file_downlaod('https://raw.githubusercontent.com/itsfoss/text-files/master/agatha.txt' , "Download.txt")


url_list  = ['https://raw.githubusercontent.com/itsfoss/text-files/master/agatha.txt','https://raw.githubusercontent.com/itsfoss/text-files/master/sherlock.txt','https://raw.githubusercontent.com/itsfoss/text-files/master/sample_log_file.txt']
file_name_list = ['DataAB.txt' , 'DataCD.txt' , 'dataXYZ.txt'] 


Ther = [threading.Thread(target=file_downlaod , args = (url_list[i] , file_name_list[i]) ) for i in range(len(url_list))]
for t in Ther : 
    t.start()  

#03 ---------------------------> ----------------------------------------> 
import time


def TIMES(id) : 
    for i in range(10) : 
        print("TIMES %d Printing %d %s" %(id,i,time.ctime()))
        time.sleep(1)

TIMES(0) 

MyThreads = [threading.Thread(target=TIMES , args  = (i,)) for i in range(3)] 
for t in MyThreads:
    t.start() 

#04 ---------------------------------------> -------------------------------------------> 
import time 
Shared_var = 0
lock_var = threading.Lock() 
def TRY(id) :  
    global Shared_var
    with lock_var:
        Shared_var = Shared_var+1
        print("TRY is %d has Increased The Shared Variable By %d " % (id ,Shared_var) ) 
        time.sleep(1)
OurThread = [threading.Thread(target=TRY , args = (i,) ) for i in range(3)]    
for t in OurThread:
    t.start() 

TRY(0) 

