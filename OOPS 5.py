#ABSTRACTION 

import abc
class PWSkills:
    @abc.abstractmethod
    def Student_Detalies(self):
        pass
    
    @abc.abstractmethod
    def Student_Assignment(self):
        pass

    @abc.abstractmethod
    def Student_Marks(self):
        pass




class Student_Detalies1(PWSkills):
    def Student_Detalies(self):
        return "THIS IS A Method FOR Taking Student Detalies" 
    
    def Student_Assignment(self):
        return "THIS IS A Method For Assign Deatalies For Particular Student" 

class Data_Science(PWSkills):
    def Student_Detalies(self):
        return "THIS WILL Return Student Detalies From Data Science"  
    
    def Student_Assignment(self):
        return "THIS WILL Give You Student Assignment Detalies From Data Science" 

DS = Data_Science()
P1 = DS.Student_Detalies() 
P2 = DS.Student_Assignment() 
SD = Student_Detalies1()
P3 = SD.Student_Detalies()
P4 = SD.Student_Assignment()
print(P3)
print(P4)
print(P1)  
print(P2) 






 