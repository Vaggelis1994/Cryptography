'''
Created on Apr 5, 2016

@author: edaravig
'''

from Crypto.Cipher import AES

import binascii
import string
import random

'''
checkECB: 

The function tests the avalanche effect of AES with ECB (Electronic Code Book).
Returns the average number of differences between the initial 
messages and the twisted ones.
'''
def checkECB (key, examples):
    
    obj = AES.new(key, AES.MODE_ECB) #generate AES object
    summed = 0
    N = 16
    
    
    for _ in range(0,examples):
        
        #generate random string with letters only (found @stack_overflow)
        message = ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(N)) 
        #print(message)
    
        #convert from string to hex
        cc1 = binascii.a2b_base64(message)
        cc2 = binascii.hexlify(cc1)
        
        #convert from hex to binary
        cc3 = bin(int(cc2, 16))[2:]

        #random bit change
        l = random.randint(0, len(cc3)-1)
    
        if cc3[l] == '0':
            cc3 = cc3[:l] + '1' + cc3[l+1:] 
        else:
            cc3 = cc3[:l] + '0' + cc3[l+1:]
    
        #convert back to string
        cc4 = hex(int(cc3, 2))[2:]
        
        #if the length of the hex result is odd turn it into even 
        #(such examples should maybe also be dumped using break)
        if (len(cc4)%2==1): cc4 += random.SystemRandom().choice(string.hexdigits)

        cc5 = binascii.unhexlify(cc4)
        
        cc6 = binascii.b2a_base64(cc5)
        message_T = cc6[:len(cc6)-1]
        #print(message_T)
        
        #encrypt original message
        ciphertext1 = obj.encrypt(message)
        ciphertext2 = binascii.hexlify(ciphertext1)
        ciphertext = bin(int(ciphertext2, 16))[2:]
        
        #encrypt twisted message
        ciphertext1_T = obj.encrypt(message_T)
        ciphertext2_T = binascii.hexlify(ciphertext1_T)
        ciphertext_T = bin(int(ciphertext2_T, 16))[2:]
        
        #two string are not always of the same length - get the minimum length
        a = len(ciphertext) if len(ciphertext) < len(ciphertext_T) else len(ciphertext_T)
        
        #compare and contrast
        diff = 0
        for l in range(0, a):
            
            if(ciphertext[l] != ciphertext_T[l]):
                diff += 1
        
        summed += (diff/len(ciphertext))
    
    return summed/examples


'''
checkCBC: 

The function tests the avalanche effect of AES with CBC.
Moreover, a pseudo - random IV is created for initialization of CBC.
Returns the average number of differences between the initial 
messages and the twisted ones.
'''
def checkCBC (key, examples):
    N = 16
    
    #pseudo - random IV generator
    IV = ''.join(random.SystemRandom().choice(string.hexdigits) for _ in range(N)) 
    
    obj = AES.new(key, AES.MODE_CBC, IV) #IV is needed
    summed = 0  
    N = 16
    
    
    for _ in range(0,examples):
        
        #generate random string with letters only (found @stack_overflow)
        message = ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(N)) 
        #print(message)
    
        #convert from string to hex
        cc1 = binascii.a2b_base64(message)
        cc2 = binascii.hexlify(cc1)
        
        #convert from hex to binary
        cc3 = bin(int(cc2, 16))[2:]

        #random bit change
        l = random.randint(0, len(cc3)-1)
    
        if cc3[l] == '0':
            cc3 = cc3[:l] + '1' + cc3[l+1:] 
        else:
            cc3 = cc3[:l] + '0' + cc3[l+1:]
    
        #convert back to string
        cc4 = hex(int(cc3, 2))[2:]
        
        #if the length of the hex result is odd turn it into even 
        #(such examples should maybe also be dumped using break)
        if (len(cc4)%2==1): cc4 += random.SystemRandom().choice(string.hexdigits)

        cc5 = binascii.unhexlify(cc4)
        
        cc6 = binascii.b2a_base64(cc5)
        message_T = cc6[:len(cc6)-1]
        #print(message_T)
        
        #encrypt original message
        ciphertext1 = obj.encrypt(message)
        ciphertext2 = binascii.hexlify(ciphertext1)
        ciphertext = bin(int(ciphertext2, 16))[2:]
        
        #encrypt twisted message
        ciphertext1_T = obj.encrypt(message_T)
        ciphertext2_T = binascii.hexlify(ciphertext1_T)
        ciphertext_T = bin(int(ciphertext2_T, 16))[2:]
        
        #two string are not always of the same length - get the minimum length
        a = len(ciphertext) if len(ciphertext) < len(ciphertext_T) else len(ciphertext_T)
        
        #compare and contrast
        diff = 0
        for l in range(0, a):
            
            if(ciphertext[l] != ciphertext_T[l]):
                diff += 1
        
        summed += (diff/len(ciphertext))
    
    return summed/examples
    

if __name__ == '__main__':
    
    key = "knapsackknapsack"
    examples = 5000
    
    resECB = checkECB(key,examples)
    print("Using", examples, "examples for testing AES with ECB, the average difference is:",resECB)
    if resECB > 0.5: 
        print("AES with ECB passes the Strict Avalanche Effect")
    else: 
        print("AES with ECB does not pass the Strict Avalanche Effect")
        error = 0.5 - resECB
        print("Error is", error)
        
    resCBC = checkCBC(key, examples)
    print("Using", examples, "examples for testing AES with CBC, the average difference is:",resCBC)
    if resECB > 0.5: 
        print("AES with CBC passes the Strict Avalanche Effect")
    else: 
        print("AES with CBC does not pass the Strict Avalanche Effect")
        error = 0.5 - resCBC
        print("Error is", error)
    