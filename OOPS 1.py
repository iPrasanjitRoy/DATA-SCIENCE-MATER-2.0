class PWSkills :
     def Welcome_msg(self): # USE Slef For USING OUTSIDE Class   (ITS NOT A RESERVE KEYWORD YOU CAN USE ANYTHINGS)  
          print("Welcome TO Physics Wallah")


Rohan = PWSkills()
Rohan.Welcome_msg() 


class PWSkills1:

    def __init__(self , phone_number , email_id, student_id): #INIT IS A Constructor 
        self.phone_number1 = phone_number
        self.email_id = email_id
        self.student_id = student_id 

    def return_student_deatials(self):
        return self.student_id  ,  self.phone_number1, self.email_id 
    
    
Rohan = PWSkills1(6295078770, "Roy@gmail.com", 101)  
AB = Rohan.return_student_deatials()
CD = Rohan.phone_number1
print(AB)  
print(CD) 




