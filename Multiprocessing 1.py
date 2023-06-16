import multiprocessing
#04 ------------->------------------->------------------------------->
import multiprocessing
def square(index , value) :
    value[index] = value[index]**2

if __name__ == '__main__':
    arr = multiprocessing.Array('i' , [2,3,4,5,6,7,8])
    process = []
    for i in range(7):
        m = multiprocessing.Process(target=square , args = (i,arr))
        process.append(m)
        m.start()
    for m in process:
        m.join()
    print(list(arr))

import multiprocessing
def sender(conn , msg) :
    for i in msg:
        conn.send(i)
    conn.close()
    
def receive(conn) : 
    while True :
        try :
            msg = conn.recv()
        except Exception as e :
            print(e)
            break 
        print(msg)

if __name__ == '__main__' :
    msg = ["My Name IS Roy" , "This IS My Messages TO Teacher" , "I Am In Class For Multiprocessing " ]  
    parent_con , child_con = multiprocessing.Pipe()
    m1  = multiprocessing.Process(target=sender , args = (child_con , msg))
    m2 = multiprocessing.Process(target=receive , args =(parent_con,))
    m1.start()
    m2.start()
    m1.join()
    child_con.close()
    m2.join()
    parent_con.close()
    
    





