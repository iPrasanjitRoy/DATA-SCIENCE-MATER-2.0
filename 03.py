Dictonary1 = { 'Name' : "Prasanjit" , 'Friend' : "Dipesh" }     
print(Dictonary1['Name'])  

list_Num = []
list_str = []
Random = [1, 2, 3, 4.0, 5.5, 'Roy', 'Kar', 200] 
for i in Random: 
    if type(i) == int or type(i) == float:
        list_Num.append(i)
    else:
        list_str.append(i)

print(list_Num)   