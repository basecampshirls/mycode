#!/usr/bin/python3
import requests

def urlpull():
#usrpull is variable from part1
#for now define usrpull as pikachu for testing
    usrpull = 'pikachu'
    pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/' + usrpull)
    link = pokemon.json()['sprites']['front_default']
    print (link)
urlpull()
