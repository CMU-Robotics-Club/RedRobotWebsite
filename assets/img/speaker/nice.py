from PIL import Image
import os

size = (200, 200)
for item in os.listdir():
    if (item.endswith("png")):
        im = Image.open(item)
        im = im.resize(size)
        #im = im.convert("RGB")
        im.save(os.path.splitext(item)[0]+"_rz.png", "PNG")
        
        