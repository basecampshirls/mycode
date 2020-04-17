#!/usr/bin/python3
import requests
import wget

dogs = requests.get("https://random.dog/woof.json")
link = dogs.json()['url']

# WGET SYNTAX
# picfilename.jpg= wget.download(url_address)

dogs.jpg = wget.download(link)
