from urllib.request import urlopen
import re

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def read(file_path):
    temp_words = set()
    with open(file_path, 'r') as file:
        i = 0
        for word_ in file:
            temp_words.add(word_)
            i+=1
            if i >= 15566: # more than 15568 produces an ERROR: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf3 in position 4382: invalid continuation byte
                break
            
    file.close()
    return temp_words

def check(url):
    if re.match(regex, url) is not None :
        RESPONSE = urlopen(url).getcode()
        if RESPONSE != 200:
            return False
            
    else:
        return False

    return True    

# Append a string to a file 
def append(file_path, data):
    with open(file_path, 'a+') as file:
        file.write(data + '\n')
    file.close()