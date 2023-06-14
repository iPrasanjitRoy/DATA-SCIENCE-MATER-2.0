#STATIC Method 

class PWSkills1 :
    
    def Student_Details(Self , Name , Email_id , Number) :
        print(Name, Email_id, Number)
        
    @staticmethod
    def Mentor_Class(list_mentor) :
        print(list_mentor)
        
    def Mentor(Self , mentor_list):
        print(mentor_list)

PWSkills1.Mentor_Class(["Prasanjit" , "Royy"])



Obj1 = PWSkills1() 
Obj1.Mentor(["Prasanjit" , "Roy", "Done"])   



#02 
class PWSkills2 : 
    def Student_Details(Self , Name , Email_id , Number) :
        print(Name, Email_id, Number)

    @staticmethod
    def Mentor_Mail_ID(Mail_ID_Mentor):
        print(Mail_ID_Mentor)   

    @staticmethod
    def Mentor_Class(list_mentor) : 
        PWSkills2.Mentor_Mail_ID(["Prasanjit@gmail.com", "Dipesh@gmail.com"]) 
        print(list_mentor) 
    
    @classmethod
    def Class_Name(Self): 
        Self.Mentor_Class(["Prasanjit" , "Dipesh"]) 

    
    def Mentor(Self, Mentor_list):
        print(Mentor_list) 
        Self.Mentor_Class(["Prasanjit" , "Dipesh"])  


PWSkills2.Mentor_Class(["Prasanjit" , "Dipesh"])   
PWSkills2.Class_Name() 
PW = PWSkills2()
PW.Mentor(["Prasanjit" , "Dipesh"])  


