#!/usr/bin/python3
import requests
import wget
import turtle
import webbrowser
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
    wget.download(dog_pic_url, '/home/student/static/dog.png')
    browser_pic(dog_pic_url)

#might need something here to convert jpg to png

#opens the picture in browser
def browser_pic(url):
    webbrowser.open(url)
    input("Press ENTER to continue.")

#show dog pic via turtle
def show_pic():
    screen = turtle.Screen()
    screen.bgpic('/home/student/static/dog.png')
    turtle.mainloop()

#probably put steganography program here

#remove('/home/student/static/dog.png')
get_pic()
#show_pic()

