'''
Created on Jun 20, 2016

@author: edaravig
'''

from math import *
from Cryptography.crt import *

#link
'''
shanks
executes the shanks function in order to find the number

'''

def shanks(a, b, p):
    
    m = int(ceil(sqrt(p)))
    L1 = []
    L2 = []
    
    inv = egcd(a, p)[1]
    if inv<0: inv+=p
    inv = (inv ** b) % p 
    
    for i in range(m):
        
        l1 = (a ** i) % p
        l2 = (b * (inv ** i)) % p
        
        L1.append(l1) 
        L2.append(l2)
    
    if (l1 == l2): return L2.index(l2) * m + 1
    
    L_common = set(L1) & set(L2)
    for l in L_common:
        q = L2.index(l)
        return q * m + 1
    
    


if __name__ == '__main__':
        
    print "Solving equation 3^x = 2, at Z_43 cyclic group. Result is:",shanks(3, 2, 43)
    print "Solving equation 3^x = 4, at Z_43 cyclic group. Result is:",shanks(3, 4, 43)
    print "Solving equation 3^x = 5, at Z_43 cyclic group. Result is:",shanks(3, 5, 43)
