"""
Unscrambles - Version 0.1

Methods:
    .unscramble(string) : Given scrambled_word, returns a tuple of all possible words it unscrambles into.
    .scramble(word: string) : Scrambles a given word.
    .exists(string) : Checks if the word exists in the provided hashed_words.json

Note: this file requires another file name hashed_words.json,
which contains by default has most of the words in the english language.

To provide a custom list of words to unscramble, see words_dict_setup.py.
"""
import json
hashed_words = open("hashed_words.json", "rt")
wordsDict = json.loads(hashed_words.read())
hashed_words.close()


def unscramble(scrambled_word):
    """
    unscramble(string) -> tuple

    Use:
        Given scrambled_word, returns a tuple of all possible words it unscrambles into.
        returns an empty tuple if no matching unscrambled words were found.

    :return:
    """
    sorted_word = ''.join(sorted(scrambled_word))
    if sorted_word in wordsDict.keys():
        return tuple(wordsDict[sorted_word])
    else:
        return ()


def exists(word):
    """
    exists(string) -> boolean

    Use:
        Checks if the word exists in the provided hashed_words.json

    :return:
    """
    sorted_word = ''.join(sorted(word))
    if sorted_word in wordsDict.keys():
        if word in wordsDict[sorted_word]:
            return True

    return False


def scramble(word):
    pass
    # TODO: this! (the scramble function)
