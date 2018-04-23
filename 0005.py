# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 21:17:30 2018
把目录里面的照片编程尺寸不大于iphone5分辨率的大小
@author: lzz
"""
from PIL import Image
import os

path = 'D:/pyjoy/learngit/0005'
resultpath = 'D:/pyjoy/learngit/0005/rel'
if not os.path.isdir(resultpath):
    os.mkdir(resultpath)
for picname in os.listdir(path):
    picpath = os.path.join(path,picname)
    with Image.open(picpath) as im:
        w,h =im.size
        n = w/1366 if(w/1366)>=(h/640) else h/640
        im.thumbnail((w/n,h/n))
        im.save(resultpath +'/finish_' +picname.split('.')[0] +'.jpg','jpeg')
        
        
