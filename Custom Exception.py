class validateage(Exception):
    
    def __init__(self , msg) : 
        self.msg = msg

def validaetage(age) : 
    if age < 0 :
        raise validateage("Entered Age is Negative " )
    elif age > 200 : 
        raise validateage("Enterd Age is Very Very High " )
    else :
        print("Age is Valid" ) 


try :
    age = int(input("Enter Your Age" ))
    validaetage(age)
except validateage as e :
    print(e) 
