#!/usr/bin/python3
import requests
import json
def pullpokemon():
    while True:
        try:
            usrpull = input("Type the name of a Pokemon! ")           
            sourc = requests.get('https://pokeapi.co/api/v2/pokemon/' + usrpull + '/')
            sourc = sourc.json()
            break
        except:
            print("Whoops! That Pokemon doesn't seem to exist!")
    return sourc
  
def main(): 
    sourc = pullpokemon()
    print(str("With our powers combined, " + (sourc['forms'][0]['name'].capitalize())) + "    , we will defeat them!\n")
  
main()

def urlpull():
#usrpull is variable from part1
#for now define usrpull as pikachu for testing
    usrpull = 'pikachu'
    pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/' + usrpull)
    link = pokemon.json()['sprites']['front_default']
    print (link)
urlpull()
