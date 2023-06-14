#Encapsulation 
class car: 
    def __init__(self, year,make,model,speed) :
        self.__year = year
        self.__make = make
        self.__model = model
        self.__speed = speed 

    def set_speed(self, speed):
            self.__speed = 0 if speed < 0  else speed 

    def get_Speed(self):
         return self.__speed 

c = car(2021, "toyata", "innova", 15)
p = c._car__year
print(p)  
c.set_speed(100)
p1 = c.get_Speed()
print(p1) 



class bank_account:
     def __init__(self, balance):
          self.__balance = balance
    
     def deposit(self, amount):
            self.__balance = self.__balance + amount 

     def withdraw(self, amount):
            if self.__balance >= amount :
                self.__balance = self.__balance - amount
                return True
            else: 
                return False 

     def get_balance(self):
            return self.__balance
     

Prasanjit = bank_account(1000)
Current_amount = Prasanjit.get_balance()
print(Current_amount)  
 