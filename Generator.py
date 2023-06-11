def Genarator(n):
    Value = 0;
    while Value <= n :
        yield Value
        Value += 1 

for Number in Genarator(5):
    print(Number) 


# Python Generator Expression 
Squares_Generator = (i * i for i in range(5)) #CREATE GENERATORS OBJECTS  

for i in Squares_Generator: 
 print(i)  