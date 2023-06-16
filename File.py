f = open("Hello.txt", 'w')
f.write('This IS My 1 File TO Write') 
f.close() 

f = open("Hello.txt", 'a')
f.write('This IS My 1 File TO Write But Dosent Delete My 1 File Info')  
f.close() 

f = open("Hello.txt", 'r')
print(f.read()) 

import os 
os.path.getsize('Hello.txt') 
# os.remove("Hello.txt") (It Delete The File) 

import shutil
shutil.copy('Hello.txt', 'COPY1.txt')
 
with open('COPY1.txt', 'r')   as ABC: 
    print(ABC.read())                                               



    