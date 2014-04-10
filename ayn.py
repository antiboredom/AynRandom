import twython
import json
import random
import re

class AynRandom(object):

    def __init__(self):
        self.phrases = []
        self.already_tweeted = [line for line in open("record.txt")]
        self.setup_twitter()

    def setup_twitter(self):
        credentials = json.load(open('credentials.json'))
        self.twitter = twython.Twython(
            credentials["api_key"],
            credentials["api_secret"],
            credentials["access_token"],
            credentials["token_secret"])

    def load_phrases(self, filename):
        self.phrases = [line.strip() for line in open(filename)]

    def load_words(self, filename):
        self.nouns = [line.strip() for line in open(filename) if line.strip() not in self.already_tweeted]

    def record(self, noun):
        recordkeeper = open("record.txt", "w");
        recordkeeper.write("%s\n" % noun)
        recordkeeper.close()

    def create_phrase(self):
        phrase = random.choice(self.phrases)
        noun = random.choice(self.nouns)
        self.record(noun)
        return phrase.replace("NOUN", noun).capitalize()

    def tweet(self):
        phrase = self.create_phrase()
        print phrase
        #self.twitter.update_status(status=phrase)


import sys

ayn = AynRandom()
ayn.load_phrases(sys.argv[1])
ayn.load_words(sys.argv[2])
ayn.tweet()
