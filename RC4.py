'''
Created on Apr 1, 2016

@author: edaravig
'''

import binascii
from Cryptography.encode import *


''' 
construct_S:

The function constructs the permutation S based on a given key 
represented as a string and then swap pseudo-randomly the elements.
'''
def construct_S (key):
    
    keylength = len(key)
    
    S = list(range(256))
    
    j = 0 
    
    for i in range(256):
        
        j = (j + S[i] + ord(key[i % keylength])) % 256
        S[i], S[j] = S[j], S[i]
        
    return S 

'''
compute_ciphertext:

The function computes the cipher text of the RC4 algorithm based on the 
text to be encrypted and the permutation S. Both inputs 
should be strings. 
'''
def compute_ciphertext (text, S):
    
    i, j = 0, 0
    
    ct = []
    
    for l in text:
        
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        
        S[i], S[j] = S[j], S[i]
        
        K = S[(S[i] + S[j]) % 256]
        ct.append(chr(ord(l) ^ K)) #http://www.joonis.de/en/code/rc4-algorithm Based on that module
        
    return "".join(ct)
    
'''
RC4_encrypt:

The function encrypts a given text using the RC4 algorithm.
After the execution, it returns the encrypted text to be sent. 
''' 
def RC4_encrypt(text, key):
    
    S = construct_S(key)
    return compute_ciphertext(text, S)     

if __name__ == "__main__":
    
    key = "MATRIX"
    
    text = "Never send a human to do a machine s job"
    text_e = text.replace(" ", "")
    text_e = text_enc(text_e)

    crypted = RC4_encrypt(text_e, key)
    
    print "Encrypted: ",text, "with key:", key, "is:", crypted        