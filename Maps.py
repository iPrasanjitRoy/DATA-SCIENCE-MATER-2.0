Number = [2,4,10,20]

def Square(Number):
    return Number * Number 


Square_Number_Iterator = map(Square, Number) #CANT APPLY WITHOUT ITERETOR 

Square_Number = list(Square_Number_Iterator)
print(Square_Number) 


#USE Lambda Function In Math 

Num0 = (1,2,3,4) 
Result = map(lambda X : X*X, Num0) 
print(Result) 

VResult = set(Result)
print(VResult)      