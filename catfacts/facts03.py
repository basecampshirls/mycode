#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')

    ## catfact is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
## print the value associated with text"
    name = r.json()["all"][0]["user"]["name"]["first"]
    print(name)
    
   # for catfact in name:
    # print(catfact["name"] + " is the lamest cat fact author.")  # the .get() method returns NONE if key not found
print (f'{main()} is the lamest cat author.')
#print ((main()) + " is the lamest cat fact author.")
#(f'{name["user"]["name"]["first"]} {name["user"]["name"]["last"]} is a dumb name.')
