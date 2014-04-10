import twython
import json
import random
import re

class AynRandom(object):

    # Instantiate the AynRandom class
    def __init__(self):
        self.phrases = []
        self.already_tweeted = [line.strip() for line in open("record.txt")]
        self.setup_twitter()

    # Load in Twitter credentials to allow for tweeting
    def setup_twitter(self):
        credentials = json.load(open('credentials.json'))
        self.twitter = twython.Twython(
            credentials["api_key"],
            credentials["api_secret"],
            credentials["access_token"],
            credentials["token_secret"])

    # Load in phrases whose blanks will be filled in randomly
    def load_phrases(self, filename):
        self.phrases = [line.strip() for line in open(filename)]

    # Load in the nouns and noun phrases that will fill in the blanks in our phrases
    def load_words(self, filename):
        # Go ahead and add it to the list of contenders if it hasn't been tweeted yet
        self.nouns = [line.strip() for line in open(filename) if line.strip() not in self.already_tweeted]
        
    # For every outgoing tweet, record the noun or noun phrase so we don't use it again later
    def record(self, noun):
        with open("record.txt", "a") as recordkeeper:
            recordkeeper.write(noun + "\n")

    # Build a tweet
    def create_phrase(self):
        # Pick a random template phrase
        phrase = random.choice(self.phrases)
        # Pick a noun from our noun & noun phrase list
        noun = random.choice(self.nouns)
        # Add the outgoing tweet to the record so we don't repeat it
        self.record(noun)
        # Capitalize the noun for proper grammar (all our phrases begin with a blank)
        noun = noun.capitalize()
        # Return the completed tweet with the noun in place
        return phrase.replace("NOUN", noun)

    # Tweet the phrase
    def tweet(self):
        phrase = self.create_phrase()
        print phrase
        self.twitter.update_status(status=phrase)


import sys

# Run the program
ayn = AynRandom()
ayn.load_phrases(sys.argv[1])
ayn.load_words(sys.argv[2])
ayn.tweet()
