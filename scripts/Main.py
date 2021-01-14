# !/usr/bin/python
# -*- coding: utf-8 -*-

import requests, json, time, random, re

#Load JSON Files
PersonalFile = json.load(open("jsons/Personal.json", "r"))
MusicFile = json.load(open("jsons/Music.json", "r"))
RandomFile = json.load(open("jsons/Random.json", "r"))
PhrasesFile = json.load(open("jsons/Phrases.json", "r"))

#Variables
Today = time.strftime("%Y-%m")

#Functions
def Choose(list):
	return random.choice(list)

def RequestApi(url):
	return requests.get(url=url).json()


#Cool things
RandomFile["IsTodayChristmas?"] = Choose(PhrasesFile["Christmas"]["yes"]) if Today == "25-12" else Choose(PhrasesFile["Christmas"]["no"])
RandomFile["IsTodayMyBirthday?"] = Choose(PhrasesFile["Birthday"]["yes"]) if Today == "07-09" else Choose(PhrasesFile["Birthday"]["no"])
RandomFile["FunFactOfTheDay"] = RequestApi("https://uselessfacts.jsph.pl/random.json?language=en")['text']
RandomFile["CoolAdviceOfTheDay"] = RequestApi("https://api.adviceslip.com/advice")['slip']['advice']
RandomFile["DadJokeOfTheDay"] = RequestApi("https://icanhazdadjoke.com/slack")['attachments'][0]['text']
PersonalFile["CurrentStackOverflowReputation"] = RequestApi("https://stackoverflow.com/users/flair/12368797.json")["reputation"]
PersonalFile["Favorites"]["Music"] = MusicFile

#Create prettified Json
will = dict(list(PersonalFile.items()) + list(RandomFile.items()))

myData = "\n```python\nwill = " + json.dumps(will, indent=5, sort_keys=True) + "\n```"

#Append new data to the README.md file
with open('README.md', 'r', encoding="utf8") as file:
    
    data = file.read().splitlines()

    start = data.index("<!--START_SECTION:mydata-->") + 1
    end = data.index("<!--END_SECTION:mydata-->") - 1

    DataTowrite = data[:start] + myData.splitlines() + data[end:]

    with open('README.md', 'w', encoding="utf8") as OutFile:
    	for item in DataTowrite:
    		OutFile.write("%s\n" % item)
