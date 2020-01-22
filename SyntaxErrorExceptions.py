# %% Syntax Error
print(9)
# print 9

int(10.0)
# int 10.0

i = 0
while(i<10):
    print(i)
    i = i+1
    
# %%  Exceptions
    
a = 10
b = "2"
liste = [1,2,3]
print(sum(liste))
# print(a+b) 
print(str(a)+b)



k = 10
zero = 0
print(k)
#a = k/zero # hata

# TRY - EXCEPT
if(zero==0):
    a = 0
else:
    a = k/zero
        
try: 
    a = k/zero
except ZeroDivisionError:
    a = 0
    
    
# Index Error
    
list1=[1,2,3,4]
list1[15] # list index out of range

# Module not found error

import numppy 

# File not found error

import pandas as pd
pd.read_csv('asd.csv') # böyle bir dosya yok

# Type error
"2"+3

#♥ Value error
int("sad")
    
# 
try:
    1/0
except:
    print("except")
else:
    print("else")
finally:
    print("done") #her türlü girer
