'''
Created on May 11, 2016

@author: edaravig
'''

'''
https://brilliant.org/wiki/extended-euclidean-algorithm/
'''

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y



def chinese(m, n):
    
    p = 1
    for mi in m:
        p *= mi
    
    M = []
    for mi in m:
        M.append(int(p/mi))

    u = []
    for i in range(len(m)):
        ui = egcd(M[i], m[i])[1]
        if ui<0: ui += m[i]
        u.append(ui)
    
    sum = 0    
    for i in range(len(n)):
        sum += u[i]*n[i]*M[i]  
    
    return sum%p    


if __name__ == '__main__':
    
    m = [17, 19, 12]
    n = [9, 13, 9]
    x = chinese(m, n)
    print(x)
    
    m = [208, 38, 32]
    n = [391, 55, 87]
    x = chinese(m, n)
    print(x)
    
    pass