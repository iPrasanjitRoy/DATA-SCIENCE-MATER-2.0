# Special (Magic or Dunder) Methods




class PWSkill : 
    def __init__(self) :
        print("THIS IS MY NEW") 

    def __init__(self) : 
        print("THIS IS MY INIT") 

        self.Mobile_Number = 1122334455 

PW = PWSkill() 
print(PW.Mobile_Number) 







#02 -------------------> ---------------------> 
class PWSkill01 : 
    def __init__(self) :

        self.Mobile_Number = 1122334455 

    def __str__(self) : 
        return "THIS IS Magic Call For STR"
 

PW1 = PWSkill01() 
print(PW1) 




