#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 15:07:52 2018

@author: user
"""

from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('/Library/Fonts/Arial.ttf', size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-60, 0), '12344566+', font=myfont, fill=fillcolor)
    img.save('result.jpg','jpeg')

    return 0
if __name__ == '__main__':
    image = Image.open('face.jpg')
    add_num(image)