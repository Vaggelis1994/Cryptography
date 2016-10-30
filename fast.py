'''
Created on Apr 20, 2016

@author: edaravig
'''
from math import floor


'''
fast:

The function computes quickly -fast- the a^g mod N formulation.
Input arguments are the basis a, the exponent g and the number N,
on which the modular division is made.

'''
def fast(a, g, N):

    #converting g from decimal to binary
    g = bin(g)
    g = g[2:len(str(g))]

    x = a #setting x equal to a
    
    delta = 1 #setting delta equal to 1
    
    for i in g:

        if (i == '1'): delta = (delta * x) % N
        
        x = (x**2) % N

    return delta 



def fast_original(b, e, m):
    
    B = b
    result = 1
    M = m 
    E = e 
        
    while (E>0):
        
        if (E%2 == 1): 
            result = (result * B) % M
        
        E = int(floor(E/2))
        B = (B**2) % M 
    
    return result
    
    
    


if __name__ == '__main__':
    
    out = fast (2, 1234567, 12345)
    print "Computing the formulation",2,"^",1234567,"mod",12345,"equals to",out
    
    out = fast (130, 7654321, 567)
    print"Computing the formulation",130,"^",7654321,"mod",567,"equals to",out

        

