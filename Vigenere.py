'''
Created on Apr 1, 2016

@author: edaravig

Credits: https://www.youtube.com/watch?v=LaWp_Kq0cKs
'''


def readText():
    
    f = open('vigenere.txt', 'r')
    text = f.read()
    f.close()
    return text

def writeText(decrypted):
    
    f = open('decrypted.txt', 'w')
    f.write(decrypted)
    f.close()
    return 

'''
IC:

The function computed the Index of Coincidence from the given text.
Returns, the Index of Coincidence and the normalized letter count 
of the given text.
'''
def IC(cipher):
    
    N = 26 #number of letters in english alphabet
    
    indexOfCoincidence = 0.0000
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    n = [0 for _ in range(N)]

    for l in cipher: 
        pos = alphabet.index(l)
        n[pos] = n[pos] + 1
    
    lengthOfCipher = len(cipher)
    
    #computes the IC according to the formulation
    for i in range(N):
        indexOfCoincidence += ( float(n[i]*(n[i]-1)) / float(lengthOfCipher*(lengthOfCipher-1)) )
        
    
    n = [float(n[i])/float(lengthOfCipher) for i in range(N)]
    #dictionary = dict(zip(list(alphabet), n))
    #sortedFreq = sorted(dictionary.items(), key = operator.itemgetter(1), reverse = True)
    return indexOfCoincidence, n

'''
decrypt:

The function decrypts the encrypted message by shifting the corresponding number of 
letter of the key. The key is repeated consistently in order to be equal to the message.
In order to find the right index of the key, a modulo operation is executed.
Returns, the plain text in lower case.
'''
def decrypt(text, key):
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = ""
    
    textSize = len(text)
    keySize = len(key)
    
    for i in range(textSize):
        e = i % keySize
        k = alphabet.index(key[e])
        
        if (alphabet.index(text[i]) - k) >= 0:#shifting back k positions
            message += alphabet[alphabet.index(text[i]) - k]#setting the deciphered letter to the message
        else:
            message += alphabet[alphabet.index(text[i]) - k + 26]
    
    return message.lower() #the deciphered message

'''
findKeyLength:

The function computes a possible key length after by computing the IC, as described above.
If the IC is close to 0.067, then there is a high probability of the correct result of the key.
The key length is finally returned. 
'''
def findKeyLength(text):

    N = 26
    k = 2
    
    textSize = len(text)
    
    found = False

    while found == False:
        col = [0 for _ in range(k)] 
        for i in range (0, k):
            col[i] = text[i:textSize-1:k]
            compute = IC(col[i])
            if (compute[0] < 0.07 and compute[0] > 0.064):
                found = True
                return k
            k = k + 1  
            if (k == N):
                break

'''
bestMatch:

The function finds the key by finding the best match between the known frequencies of the english alphabet
and the found frequencies. In order to find this, a shift is made in each round, till the end of possible shifts.
Returns the key used for decryption.
'''
def bestMatch(ic):
    
    #known frequencies of english alphabet
    frequency = [0.08167, 0.01492, 0.02782, 0.04253, 0.012702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02361, 0.00150, 0.01974, 0.00074]    
    N = len(frequency)
    
    shift = 0 #represents the shifts used to get the largest inner product of the two matrices (best match)
    bestShift = 0 
    
    bestSum = -1
        
    for _ in range(N):

        summed = 0
        
        for j in range(N - shift):
            summed += frequency[j] * ic[j + shift] 
            
        for j in range(shift):
            summed += frequency[N - shift + j] * ic[j]
            
        if summed > bestSum: 
           
            bestSum = summed
            bestShift = shift
                    
        shift += 1
    
    return bestShift

if __name__ == '__main__':
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = ""
    
    encrypted = readText()
    k = findKeyLength(encrypted)
    print(k)
    
    col = [0 for _ in range(k)]
    ic = [0 for _ in range(k)]
    textSize = len(encrypted)
    
    for i in range (0, k):
        col[i] = encrypted[i:textSize-1:k]
        ic[i] = IC(col[i])[1]
        pos = (bestMatch(ic[i])) 
        message += alphabet[pos]
       
    print(message)
    decrypted = decrypt(encrypted, message)
    
    writeText(decrypted)
    