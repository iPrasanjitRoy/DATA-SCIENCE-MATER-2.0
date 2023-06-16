try :
    f= open("Except.txt" , 'w')
    f.write(" WRITE INTO MY FILES " ) 
except Exception  as e : 
    print("THIS IS MY EXCEPT BLOCKS " , e) 
else : 
    f.close() 
    print("THIS WILL BE EXCUTED ONCE YOUR TRY EXCUTED WITHOUT ERRORS") 




try :
    f = open("Except2.txt" , 'w')
    f.write("WRITE Something" ) 
finally : 
    print("FINALLY WILL EXCUTE ITSELF IN ANY SITUATION") 


    