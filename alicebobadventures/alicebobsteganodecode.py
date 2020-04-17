#!/usr/bin/python3
from PIL import Image
import stepic
#Decode the image so as to extract the hidden data from the image
im2 = Image.open('dogtest2.jpeg')
stegoImage = stepic.decode(im2)
stegoImage
