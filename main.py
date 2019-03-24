import bs4
from bs4 import BeautifulSoup
# import keras
import requests
import lyricsgenius as genius
import re

import numpy as np
import pandas as pd


# api = genius.Genius('TzCeb4sALsjxVV6lxcKAWdQNpmZAgkJHsLYnouk5xtbUIaKFGv0_slB8K4ZrcYMr')
# artist = api.search_song('Deadpool Movie Script')
# print(artist)


#TOKEN below should be the string that the API docs tells you
#Clearly I'm not giving mine out here on the internet. That'd be dumb


# base_url = "http://api.genius.com"


#Key line below here when, this is how to authorize your request when
#using the API

#
# headers = {'Authorization': 'TzCeb4sALsjxVV6lxcKAWdQNpmZAgkJHsLYnouk5xtbUIaKFGv0_slB8K4ZrcYMr'}
# search_url = base_url + "/search"
# song_title = "In the Midst of It All"
# params = {'q': song_title}
# response = requests.get(search_url, params=params, headers=headers)

# def getCharacterLyrics(name,script):
#     print('hi')
#     # re.split('DEADPOOL:',script)


URL = 'https://genius.com/20th-century-fox-deadpool-script-annotated'
page = requests.get(URL)
html = BeautifulSoup(page.text, "html.parser") # Extract the page's HTML as a string

# Scrape the song lyrics from the HTML
# lyrics = html.find("div", class_="lyrics").get_text().encode('utf-8','ignore')
script = html.find("div", class_="lyrics").get_text()

# print(lyrics[:400])
splitScript = script.split("\n\n")
scenes = script.split("CUT TO: ")

for i in range(10):
    print(splitScript[i])
    print('\n')
# print(splitScript[:10])
print(len(splitScript))
# print(re.split('DEADPOOL:',splitScript[2]))
# print(re.split('DEADPOOL:',splitScript[3]))
# print(re.split('DEADPOOL:',splitScript[4]))
deadpoolRegexp = re.compile("DEADPOOL:(.*)$")
# print(regexp.search(splitScript[3]).group(1))
print(deadpoolRegexp.match(splitScript[3]))

print(deadpoolRegexp.search(splitScript[4]).group(1))

deadpoolLines = []
for line in splitScript:
    if deadpoolRegexp.match(line):
        deadpoolLines.append(deadpoolRegexp.search(line).group(1))
print(deadpoolLines)
print(len(deadpoolLines))

with open('deadpoolLines.txt','w') as f:
    for line in deadpoolLines:
      f.write("%s\n\n" % line)
