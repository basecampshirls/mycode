#!/usr/bin/python3
import requests
import wget
import webbrowser
import turtle
from PIL import Image
from stegano import lsb
from os import remove

#pulling random dog pic url via API and convert JSON to python
def url():
    dogs = requests.get("https://random.dog/woof.json")
    dog_api = dogs.json()
    return dog_api

#use pulled url to pull up the picture of random dog
def get_pic():
    dog_api= url()
    dog_pic_url = dog_api['url']
    wget.download(dog_pic_url, '/home/student/static/dogpics/dog.png')
    browser_pic(dog_pic_url)

#opens the picture in browser
def browser_pic(url):
    webbrowser.open(url)

#show dog pic via turtle
def show_pic():
    screen = turtle.Screen()
    screen.bgpic('/home/student/static/dogpics/dog.png')
    turtle.mainloop()

get_pic()
show_pic()

#steganography program here (Stegano)
# encode example: hide text to image
#Open Image or file in which you want to hide your data
input ("Press ENTER to continue.")
message = input ("What message do you want to hide? ")
secret = lsb.hide ("/home/student/static/dogpics/dog.png", message)
secret.save("/home/student/static/dogpics/dog2.png")
#input ("Press ENTER to continue.")

clear_message = lsb.reveal("/home/student/static/dogpics/dog2.png")
print (clear_message)

#remove('/home/student/static/dog.png')
#get_pic()
#browser_pic()

