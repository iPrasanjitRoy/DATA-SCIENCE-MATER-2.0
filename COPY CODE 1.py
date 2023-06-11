mylist = [1, 2, 3, 4, 'Prasanjit', 'Roy', [1, 2, 3, 4, 5, 6]] 


def COPYCODE(li) : 
    l = []
    for i in li :
        if type(i) == list:
            for j in i :
                l.append(j)
        else :
            if type(i) == int or type(i) == float :
                l.append(i)
    return l


Obj = COPYCODE(mylist)
print(Obj)        



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_numbers = [(lambda x: x**2)(num) for num in numbers]

print(squared_numbers)


