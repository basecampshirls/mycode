#!/usr/bin/python
import sys
print ('Basic Engineering!')
move = input ('Does it move? Type yes or no. Type q if you want to quit.')

if move.lower() == "yes":
    should1 = input ('Should it? Type yes or no. Type q if you want to quit.')
    if should1.lower() == "yes":
        print ('No problem!')
    elif should1.lower() == "no":
        print ('Put some ducktape on it.')
    elif should1.lower() == "q":
        print ('See you later!')
        sys.exit()
    else:
        print ('That is not an acceptable answer.')

elif move.lower() == "no":
    should2 = input ('Should it? Type yes or no. Type q if you want to quit.')
    if should2.lower() == "yes":
        print ('Put some WD-40 on it.')
    elif should2.lower() == "no":
        print ('No problem!')
    elif should2.lower() == "q":
        print ('See you later!')
        sys.exit()
    else:
        print ('That is not an acceptable answer.')

elif move.lower == "q":
    print ('See you later!')
    sys.exit()

else:
    print ('That is not an acceptable answer.  Please type yes or no.')
