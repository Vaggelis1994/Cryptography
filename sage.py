'''
Created on Apr 2, 2016

@author: edaravig
'''

import crypt 

'''
find:

The function executes a bruteforce trying all the combinations of
a six digit number. Each number is encrypted in order to be compared 
with the already known encrypted code. When the password is found, by 
comparison to the outcome of the encryption to the also already known
message, the password is returned and the function stops execution.
'''
def find(message, encrypted):
    
    password = 0
    for a in range(0, 1000000, 100000):
        for b in range(0, 100000, 10000):
            for c in range(0, 10000, 1000):
                for d in range(0, 1000, 100):
                    for e in range(0, 100, 10):
                        for f in range(0, 10, 1):
                            password = a + b + c + d + e + f
                            encrypted = crypt.crypt(str(password), encrypted)
                            if encrypted == message:
                                print "Password is:", password  
                                return password

def find2(message, encrypted):
    
    password = 0
    for p in range(0, 1000000):
        encrypted = crypt.crypt(str(p), encrypted)
        if encrypted == message:
            print "Password is:", password  
            return password

if __name__ == '__main__':

    message = "$6$kHnyu3Ni$EJ4BpR44aBrHZrI3NLzOlIY/g9.RADm/68NtUqp0Bxzi1SYIAqPOWrUE8ZPXyOnoOE5m9lRItkpU7PhqfkZ.f0"
    encrypted = "$6$kHnyu3Ni$"
    
    password = find2(message, encrypted)
    
    