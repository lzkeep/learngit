# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 21:05:06 2018
0004 count words
@author: lzz
"""

import os,re
def word_count(filepath):
    worddict = {}
    with open(filepath,'rt',encoding="utf8") as f:
        for line in f:
            words = re.split('[,.\s]\s*',line)
            for word in words:
                if word.lower() in worddict and word.isalpha():
                    worddict[word.lower()] +=1
                elif word.lower() not in worddict and word.isalpha():
                    worddict[word.lower()] =1
                
    wordSorted = sorted(zip(worddict.keys(),worddict.values()))
    
    for word,count in wordSorted:
        print(word,":",count)
        
        
if __name__ == '__main__':
    word_count(r'D:/pyjoy/program/0004.txt')
    
    
    