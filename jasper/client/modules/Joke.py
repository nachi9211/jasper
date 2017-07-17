# -*- coding: utf-8-*-
import random
import re
from client import jasperpath

WORDS = ["JOKE", "LAUGH"]


def getRandomJoke(filename=jasperpath.data('text', 'JOKES.txt')):
    jokeFile = open(filename, "r")
    jokes = []
    start = ""
    end = ""
    for line in jokeFile.readlines():
        line = line.replace("\n", "")

        if start == "":
            start = line
            continue

        if end == "":
            end = line
            continue

        jokes.append((start, end))
        start = ""
        end = ""

    jokes.append((start, end))
    joke = random.choice(jokes)
    return joke


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by telling a joke.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    joke = getRandomJoke()

    #mic.say("Knock knock")

    def firstLine():
        def punchLine():
            mic.say(joke[1])

        mic.say(joke[0])

        mic.say('Should I Finish?')
        
        choice = mic.activeListen()
        if choice.lower() = 'yes':
            punchLine()
        else:
            mic.say('Ok, bye bitch')

    firstLine()


def isValid(text):
    """
        Returns True if the input is related to jokes/humor.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    if bool(re.search(r'\blaugh\b', text, re.IGNORECASE)):
        return True    
    elif bool(re.search(r'\bjoke\b', text, re.IGNORECASE)):
        return True
    else:
	return False
