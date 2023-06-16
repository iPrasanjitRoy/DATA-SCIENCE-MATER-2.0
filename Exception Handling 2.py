try :     
    a = 10/0
except ZeroDivisionError as e :
    print(e)
    
try :
    int("ROY")
except (ValueError , TypeError) as e :
    print(e)

try :
    int("ROY")
except:
    print("this will catch an error")

try :
    import Roy 
except ImportError as e :
    print(e)
10/4

try :
    d = {"Key" :"Roy" , 1 : [2,3,4,5]} 
    print(d["Key2"])
except KeyError as e : 
    print(e) 

try : 
    "ROY".test()
except AttributeError as e :
    print(e)

try :
    l = [2,3,4,5]
    print(l[6])
except IndexError as e :
    print(e) 

try :
    123 + "ROY" 
except TypeError as e :
    print(e)    

try :
    with open("NOFile.txt" , 'r') as f :
        test = f.read()
except FileNotFoundError as e :
    print(e) 

try :
    with open("NoFiles.txt" , 'r') as f :
        test = f.read()
except Exception as e :
    print(e)
except FileNotFoundError as e :
    print("Files " , e)  

def TEST(file):
    try :
        with open(file , 'r') as f :
            TEST = f.read() 
    except Exception as e :
        print(e)
    except FileNotFoundError as e :
        print("TEST " , e) 