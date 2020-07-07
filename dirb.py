import os
from methods import *

FILE_NAME = 'small.txt'
RESULTS_FILE = 'results.txt'
words = read(FILE_NAME)

CORRECT = False
BASE_URL = ''
while not CORRECT:
    CORRECT = True
    BASE_URL = input('Enter The website URL:\t')

    if check(BASE_URL):
        CORRECT = True
    else:
        CORRECT = False
        print ("WRONG URL.") 

for word in words:
    for i in range(4):
        TEMP = BASE_URL
        TEMP += '/' + word.replace('\n', '')
        if i == 0:
            TEMP = TEMP + '.html'
        elif i == 1:
            TEMP += '.php'
        elif i == 2:
            TEMP += '.txt'
        elif i == 3:
            TEMP += '.pdf'

        if check(TEMP):
            print (TEMP)
            append(RESULTS_FILE, TEMP)
            
print('DONE')

