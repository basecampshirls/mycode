#!/usr/bin/python3
import rsa
#Alice's generated key pair, Bob has public Alice's public key
(alice_pub, alice_priv) = rsa.newkeys(512)

#Bob uses Alice's public key to encrypt message to Alice
bobmessage = input ('What is the message you want to send? ')
message = bobmessage.encode('utf8')
crypto = rsa.encrypt(message, alice_pub)

#Here is the encrypted message
input ('Press ENTER to see the encrypted message.')
print (crypto)

#Insert steganography program here

input ('Press ENTER to continue.')

#Alice uses her private key to decrypt Bob's message
message = rsa.decrypt(crypto, alice_priv)

print(message.decode('utf8'))

