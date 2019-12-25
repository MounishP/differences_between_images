# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 23:17:12 2019

@author: Mahesh
"""

from PIL import Image ,ImageChops
img1=Image.open("1.jpg")
img2=Image.open("2.jpg")
diff=ImageChops.difference(img1,img2)
if diff.getbbox():
	diff.show()