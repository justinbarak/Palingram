""" created at the start of the palingram project 
    to download the dictionary for the palingram.
    justinbarak 11/22/2020
"""

import requests
import os

link = "http://inventwithpython.com/dictionary.txt"
filename = "dictionary.txt"

r = requests.get(link)
textfile = open(os.path.join(r".\Palingram", filename), "w")
textfile.write(r.text)
textfile.close()
