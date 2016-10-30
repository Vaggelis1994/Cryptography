'''
Created on Apr 1, 2016

@author: edaravig
'''

import zipfile

def findPassword (filename, dictionary):
    
    words = open(dictionary, 'r') #open file with the words of the dictionary
    zFile = zipfile.ZipFile(filename) #point to the zip file 
    
    #executing bruteforce in order to find the password
    for w in words:

        try:
            zFile.extractall(pwd = w[0:len(w)-1]) #checking if the word is the password
            print "Password is:", w
            break
        except:
            pass

    #closing the streams
    words.close() 
    zFile.close()        

if __name__ == '__main__':
    
    zipname = "test_zip.zip"
    dictionary = "english.txt"
    
    findPassword(zipname, dictionary)