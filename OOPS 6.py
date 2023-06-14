#DECORATOR

def deco(func):
    def inner_deco():
        print("THIS IS MY Start")
        func()
        print("THIS IS MY End") 
    return inner_deco 

@deco
def Inside_Function():
    print(100+1001) 

Inside_Function() 
