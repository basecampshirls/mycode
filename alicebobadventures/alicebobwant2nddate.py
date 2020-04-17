#!/usr/bin/python3

import sys

print('This is a cryptography game.')

startgame = input('Are you ready to play? Type yes if you are.')

if startgame.lower() == "yes":
    print ('Alright, let me set the scene for how our adventure begins')

elif startgame.lower() != "yes":
    print ('Well thanks for checking out the game. See ya!')
    sys.exit()

print('Bob is a space enthusiast, and loves the great outdoors.\nAlice is a bookworm, and dog photographer. \nOne bright summer day, Alice decided to take a ferry ride to the San Juan Islands to photograph orcas and met Bob, who was getting ready for an ocean kayaking adventure. \nThey hit it off right away and exchanged emails (because you know, they just met and a cell phone number would be moving too fast, lol). \nBob was excited to get Alice\'s email, and immediately scheduled to meet up again.\nHowever, little did Bob know, his crazy stalker (who claims to be his girlfriend), Evil Eve, had figure out a way to access his plaintext messages and plotted to crash his date. \nLuckily, Bob figured it out Evil Eve\'s plans before his date and now needs to securely email Alice again so he can reschedule the date.')

