# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 20:47:39 2018
0001Register caode
@author: lzz
"""

import random, string

forselect = string.ascii_letters + "0123456789"

def generate(count,length):
    for x in range(count):
        Re = ""
        for y in range(length):
            Re +=random.choice(forselect)
        print(Re)
        
if __name__=="__main__":
    generate(200,10)