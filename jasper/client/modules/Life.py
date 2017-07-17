# -*- coding: utf-8-*-
import random
import re

WORDS = ["MEANING", "OF", "SEX"]


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    messages = ["It's 69, you idiot.",
		"it is 69, you virgin fuck.",
                "It's 69. How many times do I have to tell you?"]

    message = random.choice(messages)

    mic.say(message)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bmeaning of sex\b', text, re.IGNORECASE))
