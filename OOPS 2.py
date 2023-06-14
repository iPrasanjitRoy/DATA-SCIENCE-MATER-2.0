# POLYMORPHISM 
class Data_Science: 
    def Syallabus(self):
        print("THIS IS MY SYALLABUS FOR DATA SCIENCE")

class Web_Dev:
    def Syallabus(self):
        print("THIS IS MY SYALLABUS FOR WEB DEV") 


def class_parcer(class_obj):
    for i in class_obj:
        i.Syallabus()

Data_Science = Data_Science() 
Web_Dev = Web_Dev() 

class_obj = [Data_Science, Web_Dev] 
class_parcer(class_obj) 
