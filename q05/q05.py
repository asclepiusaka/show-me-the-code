import os
from PIL import Image

IP5resolution=(1136,640)

resourcePath='./pic'
files = os.listdir(resourcePath)
filtered = []
for f in files:
    fullpath = os.path.join(resourcePath, f)
    if(os.path.isfile(fullpath)):
        filtered.append(fullpath)

for f in filtered:
    im = Image.open(f)
    if im.size[0]>IP5resolution[0]:
        im = im.resize((1136,im.size[1]*1136//im.size[0]))
    elif im.size[1]>IP5resolution[1]:
        im = im.resize((im.size[0]*640//im.size[1],640))
    element=f.split('.')
    im.save('.'+element[1]+'-modified.'+element[2])


