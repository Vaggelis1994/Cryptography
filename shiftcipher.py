'''
Created on Apr 1, 2016

@author: edaravig
'''

'''
shifted:

The function executes a shift decryption by using all the possible elements -letters-
of an alphabet and making the shifts using the encrypted message given as an argument. 
A list of the results is returned in the end. The user must recognize by its own 
which of the results is the appropriate one.

'''
def shifted(encrypted, table):

    message = [] 
    mes = "" #empty string represents the deciphered message for each e
    
    for e in range (24):#searching all the possible values of e (0-23) -brute-force

        length = len(encrypted)
        for i in range(length):
        
            if (table.index(encrypted[i]) - e) >= 0:#shifting back e positions
                mes += table[table.index(encrypted[i]) - e]#setting the deciphered letter to the message
            else:
                mes += table[table.index(encrypted[i]) - e + 24] #shifting back e positions and front 23 -cases that the difference is a negative number
                    
        message.append(mes) #append each result to the list
        mes = "" #clearing the message to get the new one
        
    return message    


if __name__ == '__main__':

    encrypted = "ΟΚΗΘΜΦΔΖΘΓΟΘΧΥΚΧΣΦΘΜΦΜΧΓΟΣΨΧΚΠΦΧΘΖΚΠ"

    #represents the greek alphabet
    table = [ 'Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ',
              'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω' ]

    
    results = shifted(encrypted, table)
    for r in results:
        print(r)
    

    
    
