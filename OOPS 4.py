#Inheritance 

class Test:
    def Test_Method(self):
        return "THIS IS MY 1 CLASS"
    
class Child_Test(Test):
    pass 

Child_Test_Object = Child_Test()
P1 = Child_Test_Object.Test_Method() 
print(P1) 