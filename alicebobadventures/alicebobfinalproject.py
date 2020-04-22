#!/usr/bin/python3
import sys
import rsa
import requests
import wget
import webbrowser
import turtle
from PIL import Image
from stegano import lsb
from os import remove

print ('This is a cryptography inspired tutorial.')

#Using if/elif to let player choose if they want to proceed with the tutorial
startgame = input ('Are you ready to start? Type YES if you are. ')
if startgame.lower() == "yes":
    print ('Alright, let me set the scene for how our adventure begins. \n')
elif startgame.lower() != "yes":
    print ('Well thanks for checking out the tutorial. See ya!')
    sys.exit()

#Tutorial Scene Setter
print ('Bob is a space enthusiast, and loves the great outdoors.\nAlice is a bookworm, and dog photographer. \nOne bright summer day, Alice decided to take a ferry ride to the San Juan Islands to photograph orcas and met Bob, who was getting ready for an ocean kayaking adventure. \nThey hit it off right away and exchanged emails (because you know, they just met and a cell phone number would be moving too fast, lol).\n')
input ('Press ENTER to continue.')
print ('\nBob was excited to get Alice\'s email, and immediately scheduled to meet up again.\nHowever, little did Bob know, his crazy stalker (who claims to be his girlfriend), Evil Eve, had figure out a way to access his plaintext messages and plotted to crash his date. \nLuckily, Bob figured it out Evil Eve\'s plans before his date and now needs to securely email Alice again so he can reschedule the date.\n')

#Another if/elif to let the player choose if they want to proceed with the tutorial, also to insert natural transition breaks to the next part of the tutorial
continuegame = input ('Think you can help Bob out? Type YES if you can. ')
if continuegame.lower() == "yes":
    print ('Great, Bob really needs some help with this.')
    input ('Press ENTER to help Bob encrypt his message to Alice.')
elif continuegame.lower() != "yes":
    print ('Aww man, that sucks.  Unfortunately without your help, Evil Eve figured out how to crash Bob and Alice\'s second date and that ends the Alice and Bob story.')
    sys.exit()

#Let's start the encryption portion
print ('\nAlrighty, thanks for agreeing to help Bob out. Honestly, Bob is kind of a doof and would not be able to do this without you. Here is the plan. You will need to encrypt Bob\'s message to Alice first. Don\'t know how to do that? Don\'t worry, let\'s walk through this step by step.')
input ('Press ENTER to run the RSA Encryption Program.')

#Insert RSA Encryption Program here (this is where the rsa module gets used)
#Alice's generated key pair, Bob has public Alice's public key
(alice_pub, alice_priv) = rsa.newkeys(512)
#Need Alice's private key later to decrypt message, so making a global variable
ALICE_PRIV = alice_priv

#Bob uses Alice's public key to encrypt message to Alice
bobmessage = input ('What is the message you want to send? ')
message = bobmessage.encode('utf8')
#Need CRYPTO to be global so we can call this variable later when Alice decrypts the encrypted message
CRYPTO = rsa.encrypt(message, alice_pub)

#Here is the encrypted message
input ('Press ENTER to see the encrypted message.')
print ('\nGreat job! Here is the encrypted message:' + ' \n' + str(CRYPTO))

input ('Press ENTER to continue with the tutorial.')
print ('\nGreat! That looks pretty confidential. Now Evil Eve won\'t be able to figure out when to crash Bob\'s date with Alice. \nHowever, Evil Eve is a pretty conniving person. \nIf she found out Bob is making plans with Alice, it might drive her crazy and who know how else she might plot to harass them.... \nMaybe it would be best if Evil Eve is oblivious to the fact that Bob is even arranging a date with Alice. \nMaybe...Bob can send Alice a dog picture. \nAlice LOVES dogs and dog pictures are pretty innocent right?')
input ('Press ENTER if you want to help Bob hide his encrypted message to Alice in a dog picture.')

print ('\nFirst let\'s find a dog picture to use.')
input ('Press ENTER to pull a random dog picture from the internet using API.')

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
    input ('Press ENTER to continue.')

#steganography program here (Stegano)
print ('Alright let\'s hide that message!')
input ("Press ENTER to take the encrypted message and hide it in the dog picture using a steganography program.")
secret = lsb.hide ("/home/student/static/dogpics/dog.png", str(CRYPTO))
secret.save("/home/student/static/dogpics/dog2.png")

print ('\nSuccess! Looks like this message is ready to be emailed out to Alice. Thanks for all your help!')

#These next lines clear the dogpics folder so that this tutorial can be ran again. 
#Commented off the lines for project presentation purposes
#remove('/home/student/static/dogpics/dog.png')
#remove('/home/student/static/dogpics/dog2.png')
