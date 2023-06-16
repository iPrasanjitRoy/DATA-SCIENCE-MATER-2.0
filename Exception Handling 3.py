#use always a specific exception
try :
    10/0
except Exception as e :
    print(e) 


#print always a proper message 
try :
    10/0
except ZeroDivisionError as e :
    print("i am trying to handle a zerodivision error"  , e)


#always try to log your error
import logging
logging.basicConfig(filename = "error.log" , level = logging.ERROR)
try :
    10/0
except ZeroDivisionError as e :
    logging.error("i am trying to handle a zerodivision error {} ".format(e) ) 

#alwyas avoid to write a multiple exception handling 
try :
    10/0
except FileNotFoundError as e : 
    logging.error("i am handling file not found  {} ".format(e) )
except AttributeError as e : 
    logging.error("i am handling Attribute erro  {} ".format(e) )
except ZeroDivisionError as e :
    logging.error("i am trying to handle a zerodivision error {} ".format(e) ) 


#Document all the error 
#cleanup all the resources
try :
    with open("test.txt" , 'w') as f :
        f.write("this is my data to file " )
except FileNotFoundError as e : 
    logging.error("i am handling file not found  {} ".format(e) )
finally :
    f.close() 

