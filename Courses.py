import os, sys
from os.path import dirname, join, abspath 

sys.path.insert(0, abspath(join(dirname(__file__),"..")))  

from Payment  import Payment  
 
def course():
    print("THIS IS MY COURSE DETAILS") 

Payment.payment()  


