#!/usr/bin/env python3

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

im = Image.open("resource.jpg")
fnt = ImageFont.truetype("msyh.ttf",80)
try:
    str_num = input("input the number you want to display:")
    num = int(str_num)
except:
    print("the input is not a number")
        
pos = (im.size[0]//5*4,im.size[1]//10*1)
imd = ImageDraw.Draw(im)
imd.text(pos,str(num),font=fnt,fill=(255,0,0))
im.save("resouce1.jpg")
