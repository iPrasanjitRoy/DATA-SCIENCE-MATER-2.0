#Class Method 
class PWSkills: 
    def __init__(self, name, email) :
        self.name = name 
        self.email = email

    def Student_Detalies(self):
        print(self.name, self.email) 

PW1 = PWSkills("Prasanjit", "Roy@gmail.com")
print(PW1.name) 
PW1.Student_Detalies() 



# Class Method ---> ---> ----> ----->  
class PWSkills1:
    def __init__(self, name, email):
        self.name = name
        self.email = email 

    @classmethod
    def Student_Detalies(self, name, email) :
        return self(name , email) 
    
    def Student(self): 
        print(self.name, self.email) 


PW2 = PWSkills1.Student_Detalies("Roy", "Prasanjit@gmail.com") #Method Calling 
PW2.Student() 

#02 -----> ------> -------> -------> 
class PWSkills2: 
    Mobile_Number = 998877554400
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    @classmethod
    def Change_Number(ABC, Mobile) :
        PWSkills2.Mobile_Number = Mobile

    @classmethod
    def Student_Detalies(self, name, email) :
        return self(name , email) 
    
    def Student(self): 
        print(self.name, self.email, PWSkills2.Mobile_Number) 


PWX = PWSkills2.Student_Detalies("Dipesh", "Guragain@gmail.com" ) 
PWX.Student() 

PWSkills2.Change_Number(1122334455)
print(PWSkills2.Mobile_Number) 





#03 -----> ------> -------> -------> 
class PWSkills3: 
    Mobile_Number = 998877554400
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    @classmethod
    def Change_Number(ABC, Mobile) :
        PWSkills2.Mobile_Number = Mobile

    @classmethod
    def Student_Detalies(self, name, email) :
        return self(name , email) 
    
    def Student(self): 
        print(self.name, self.email, PWSkills2.Mobile_Number) 

#OUTER FUNCTION
def Courses_Detailes(Self, Course) : 
    print("COURSE NAME IS", Course) 

PWSkills3.Courses_Detailes = classmethod(Courses_Detailes) 
PWSkills3.Courses_Detailes(["Data Science Master", "Java"])  


#04 -----> ------> -------> -------> 
class PWSkills4: 
    Mobile_Number = 998877554400
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    @classmethod
    def Change_Number(ABC, Mobile) :
        PWSkills2.Mobile_Number = Mobile

    @classmethod
    def Student_Detalies(self, name, email) :
        return self(name , email) 
    
    def Student(self): 
        print(self.name, self.email, PWSkills2.Mobile_Number) 


del PWSkills4.Change_Number #DELETE THE FUNCTION 
delattr (PWSkills4, "Student") 
""" 
PWSkills4.Change_Number(1122334455) 
print(PWSkills4.Mobile_Number)  

"""

