# Property Decorators - Getters, Setters, And Deletes

class PWSkills  :
    
    def __init__(self , Course_Price , Coruse_Name): 
        
        self.__Course_Price = Course_Price # Making It Private 
        self.Course_Name = Coruse_Name
        
    @property #Acsessing It By USING 
    def Course_Price_Access(self) : 
        return self.__Course_Price 
    
    @Course_Price_Access.setter
    def Course_Price_Set(self , Price ): 
        if Price <= 3500: 
            pass
        else :
            self.__Course_Price = Price
            
    @Course_Price_Access.deleter
    def Delete_Course_Price(self) : 
        del self.__Course_Price
    
  
PW1 = PWSkills(3500 , "data science masters") 
print(PW1.Course_Price_Access) 


