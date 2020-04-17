#!/usr/bin/python3
# encode example: hide text to image
from PIL import Image
import stepic
#Open Image or file in which you want to hide your data
im = Image.open('dogpic.jpg')
#Convert .jpg to .png otherwise this program will not work
im.save('dogpic.png')
#Encode some text into your Image file and save it in another file
im1 = stepic.encode(im, b'This is a test')
im1.save('dogpic2.png', 'png')
#Now is the time to check both images and see if there is any visible changes
im1 = Image.open('dogpic2.png')
im1.show()
#Decode the image so as to extract the hidden data from the image 
im2 = Image.open('dogpic2.png')
stegoImage = stepic.decode(im2)
stegoImage

