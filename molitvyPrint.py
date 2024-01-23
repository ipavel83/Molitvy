#py3.7

import sys
import time
import unicodedata

# https://stackoverflow.com/questions/61601610/removing-all-non-letter-chars-from-a-string-with-accents-in-python?rq=3
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def printMolitvu(textArray, times):
    for num in range(0,times):
        for t in textArray:   
            print(t)
            time.sleep(0.05*len(t))

if __name__ == '__main__':

    filename = "molitvySome.txt"

    try:
        with open(filename, encoding="utf8") as txt:
            textToExtract =txt.read()
            textAsArray = strip_accents(textToExtract).splitlines()
            
            t = []
            times = 0;
            
            for s in textAsArray:
                if(s == ''):
                    if t != []:
                        printMolitvu(t, times);
                        
                    t = []
                    times = 0;
                    
                    time.sleep(1)
                elif (s[0] == '\t'):
                    for tabs in s:
                        if tabs == '\t':
                            times = times + 1
                            
                t.append(s)
        
    except IOError:
        print(f"can't open file {filename}")

input()


    
    