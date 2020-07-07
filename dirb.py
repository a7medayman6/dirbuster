import os
from methods import *

FILE_NAME = 'big.txt'
words = read(FILE_NAME)

CORRECT = True
BASE_URL = ''
while not CORRECT:
    BASE_URL = input('Enter The website URL:\t')
    if check(BASE_URL):
        CORRECT = True
    else:
        CORRECT = False
        print ("WRONG URL.") 

for word in words:
    TEMP = BASE_URL
    TEMP += '/' + word
    if check(TEMP):
        print (TEMP)
        append(FILE_NAME, TEMP)

print('DONE')
