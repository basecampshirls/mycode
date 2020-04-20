#!/usr/bin/python3

import sys

print ('This is a cryptography inspired tutorial.')

#Using if/elif/else to let player choose if they want to proceed with the tutorial
startgame = input ('Are you ready to start? Type yes if you are.')
if startgame.lower() == "yes":
    print ('Alright, let me set the scene for how our adventure begins')
    break
elif startgame.lower() == "no":
    print ('Well thanks for checking out the tutorial. See ya!')
    sys.exit()
else startgame.lower() != "yes" and != "no":
    print ('That is not a valid response')

#Tutorial Scene Setter
print ('Bob is a space enthusiast, and loves the great outdoors.\nAlice is a bookworm, and dog photographer. \nOne bright summer day, Alice decided to take a ferry ride to the San Juan Islands to photograph orcas and met Bob, who was getting ready for an ocean kayaking adventure. \nThey hit it off right away and exchanged emails (because you know, they just met and a cell phone number would be moving too fast, lol). \nBob was excited to get Alice\'s email, and immediately scheduled to meet up again.\nHowever, little did Bob know, his crazy stalker (who claims to be his girlfriend), Evil Eve, had figure out a way to access his plaintext messages and plotted to crash his date. \nLuckily, Bob figured it out Evil Eve\'s plans before his date and now needs to securely email Alice again so he can reschedule the date.')

#Another if/elif/else to let the player choose if they want to proceed with the tutorial, also to insert natural transition breaks to the next part of the tutorial
continuegame = input ('Think you can help Bob out? Type yes if you can. ')
if continuegame.lower() == "yes":
    print ('Great, Bob really needs some help with this.')
    input ('Press ENTER to help Bob encrypt his message to Alice.')
    break
elif continuegame.lower() == "no":
    print ('Aww man, that sucks.  Unfortunately without your help, Evil Eve figured out how to crash Bob and Alice\'s second date and that ends the Alice and Bob story.')
    sys.exit()
else continuegame.lower() != "yes" and != "no":
    print ('Seriously, type in a valid response. It\'s either yes or no.')

#Let's start the encryption portion
print ('Alrighty, thanks for agreeing to help Bob out. Honestly, Bob is kind of a doof and would not be able to do this without you. Here is the plan. You will need to encrypt Bob\'s message to Alice first. Don\'t know how to do that? Don\'t worry, let\'s walk through this step by step.')
input ('Press ENTER to run the RSA Encryption Program.')

#Insert RSA Encryption Program here

