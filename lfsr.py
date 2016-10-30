'''
Created on Apr 5, 2016

@author: edaravig
'''

from Cryptography.encode import *

def readText(filename):
    
    f = open(filename, 'r')
    text = f.read()
    text = text[1:len(text)-1]
    f.close()
    return text

'''
keystream:

The function computes the given input to the lfsr, by finding the 
keystream that was used for an encryption.

'''
def getKeystream(enc1, enc2):
    encoded1 = text_enc(enc1)
    encoded2 = text_enc(enc2)
    xored = string_xor(encoded1, encoded2)
    keystream = xored[::-1]
    return keystream

'''
sage:

The code that was used in sage in order to make computations between 
matrices. In detailed, a rollback method is implemented in order to find 
the initial state - seed of the lfsr given that i-th state is known.
'''
def sage():
    #code from sage
    #N = 10
    #a = Matrix([1, 0, 0, 0, 1, 0, 1, 0, 0, 1]) #a=keystream 
    #B = Matrix(ZZ,N,N)
    #for i in range(N-1):
    #    B[i+1, i] = 1
    #B[0] = [0,0,0,0,0,1,1,0,1,1]
    #for i in range(10):
    #    a = a.transpose()
    #    x = B.solve_right(a)
    #    a = x.transpose()
    #    for i in range(a.ncols()):
    #        a[0,i] = a[0,i]%2
    #seed = a
    seed1 = [1,1,0,0,1,0,1,0,1,1]
    return seed1

'''
decrypt:

The function decrypts the message to the plaintext, by using the constructed lfsr.
The seed was generated from the code of sage. Returns the plain text. 

'''
def decrypt(text, keystream, seed):
    
    encoded = text_enc(text)
    bits = len(encoded)
    feedback = [0,0,0,0,0,1,1,0,1,1]
    
    stream = lfsr(seed, feedback, bits, 1)
    plaintext_enc = string_xor(encoded, stream)
    return text_dec(plaintext_enc)
     


if __name__ == '__main__':
    sageResults = sage()
    
    text = readText('lfsr1.txt')
    keystream = getKeystream("ab", "sq")
    plain = decrypt(text, keystream, sageResults)
    print(plain)
    
    feedback1 = [0,0,0,0,0,1,1,0,1,1]
    feedback2 = [0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1]
    text = readText('lfsr2.txt')
    keystream = getKeystream("abcd", "!c.)")
