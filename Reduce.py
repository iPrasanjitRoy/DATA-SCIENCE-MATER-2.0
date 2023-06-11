from functools import reduce 

Num = [1, 2, 3, 4] 
Ans = reduce(lambda x, y : x+y, Num)
print(Ans) 

def product(x,y):
    return x*y

ans = reduce( product, [1, 2, 10]) 
print(ans) 


 