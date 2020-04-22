#!/usr/bin/python3
import requests
import wget
import webbrowser
import turtle
from PIL import Image
from stegano import lsb

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
try:
    show_pic()
except:
    input ('Got the dog picture. Press ENTER to run the steganography program.')

#steganography program here (Stegano)
print ('Alright let\'s hide that message!')
message = input ("What is the message you want to hide? ")
#hide message
secret = lsb.hide ("/home/student/static/dogpics/dog.png", message)
secret.save("/home/student/static/dogpics/dog2.png")
#unhide message
input ('Want to see the hidden message? Press ENTER.')
clear_message = lsb.reveal("/home/student/static/dogpics/dog2.png")
print ('Here is the hidden message.')
print ('\n' + clear_message)


