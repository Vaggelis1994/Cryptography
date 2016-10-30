'''
Created on May 11, 2016

@author: edaravig
'''
from Crypto.Random.random import randint
from fractions import gcd
from Cryptography.fast import *


'''

Fermat's check algorithm

'''
def fermat(n):
    
    a = randint(2, n-2)
    
    if (gcd(a,n)>1):
        return "composite"
    r = fast(a, n-1, n)
    if(r==1):
        return "prime"
    else:
        return "composite"
    
    
'''
Function used

'''
def func(x):
    return abs(x**2+x-1354363)



if __name__ == '__main__':
            
    for _ in range(100):
        
        n = randint(1, 10000)
        f = func(n)
        who = fermat(f)
        
        if (who=="prime"): print("Number",n,"is",who)
        
        