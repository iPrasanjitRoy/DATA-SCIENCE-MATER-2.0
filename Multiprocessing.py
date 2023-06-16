import multiprocessing 
def TEST():
    print("THIS IS MY MULTIPROCESSING PROGRAMS") 

if __name__ == '__main__': 
    M  = multiprocessing.Process(target=TEST) 
    print("THIS IS MY 1 MAIN Programmes")
    M.start()
    M.join()  


#02 -------------------> ------------------------> 
def square(n):
    return n**2

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool : 
        out = pool.map(square , [1,2,3,4,5,6,7,8,9])
        print(out)

#03 -------------> ----------------------> 
import multiprocessing
def producer(q) :
    for i in ["Prasanjit", "Roy" , "Dipesh"]: 
        q.put(i)
    
def consume(q) :
    while True : 
        item = q.get()
        if item is None :
            break
        print(item)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    m1 = multiprocessing.Process(target=producer , args= (queue,))
    m2 = multiprocessing.Process(target=consume , args = (queue,))
    m1.start()
    m2.start()
    queue.put("Guragain")
    m1.join()
    m2.join()

