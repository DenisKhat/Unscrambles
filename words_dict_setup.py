"""
Denis Khatnyuk - 2022

A script which parses a given file in the same subdirectory named words.txt, into a format more easily readable
and which will work more efficiently in python. (For use with unscrambles.py)
"""

import json
import sys

try:
    wordsFile = open("words.txt", "rt")
except FileNotFoundError:
    print("No word file found")
    sys.exit()

# Step one is to create the actual dictionary which will contain all the words.
# The keys will be the words, alphabetically sorted.

outputDict = {}

for word in wordsFile.read().split():
    sorted_word = "".join(sorted(word)) #
    if sorted_word in outputDict.keys():
        outputDict[sorted_word].append(word)
    else:
        outputDict[sorted_word] = [word]
wordsFile.close()

# Now dump the dictionary into a new file:

outputFile = open("hashed_words.json", "wt")
outputFile.write(json.dumps(outputDict, sort_keys=True, indent=4))
outputFile.close()
