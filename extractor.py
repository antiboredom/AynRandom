import re
from textblob import TextBlob

def nouns(input_filename, output_filename):
    with open(input_filename, 'r') as content_file:
        text = content_file.read()

    #text = text.decode('utf-8')
    noun_phrases = TextBlob(text).noun_phrases
    nouns = [word[0] for word in TextBlob(text).tags if word[1] == "NN"]
    current_phrases = [line for line in open(output_filename)]
    phrases = current_phrases + noun_phrases + nouns

    output_set = set()
    for phrase in phrases:
        phrase = re.sub(r'[\W_]$', '', phrase)
        phrase = phrase.replace(" '", "'")
        output_set.add(phrase)

    output_file = open(output_filename, 'w')
    for phrase in output_set:
      output_file.write("%s\n" % phrase)


import sys
nouns(sys.argv[1], sys.argv[2])
