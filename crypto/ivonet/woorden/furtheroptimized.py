#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import time
import unicodedata

alphabet = ''.join(chr(ord('a') + i) for i in range(26))
rec = re.compile('[^a-z]')
realFreqs = {'e': 0.1891, 'n': 0.1003, 'a': 0.0749, 't': 0.0679, 'i': 0.065, 'r': 0.0641, 'o': 0.0606, 'd': 0.0593,
             's': 0.0373, 'l': 0.0357, 'g': 0.034, 'v': 0.0285, 'h': 0.0238, 'k': 0.0225, 'm': 0.0221, 'u': 0.0199,
             'b': 0.0158, 'p': 0.0157, 'w': 0.0152, 'j': 0.0146, 'z': 0.0139, 'c': 0.0124, 'f': 0.0081, 'x': 0.0004,
             'y': 0.0035, 'q': 0.0009}


def prepWord(string):
    '''
    Removes accents from all characters in string and makes it lowercase
    '''
    return unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore').decode('utf-8').lower()


def prepWords(string):
    '''
    Calls prepWord on string and splits string at every non-alpha character
    '''
    return rec.split(prepWord(string))


def loadWordList(fileName='woordenlijstNLTotaal.txt'):
    '''
    Load all words from fileName
    Returns dictionary with all words with its type as key
    '''
    # Time it
    t = time.time()
    # Read raw input from file
    rawWords = []
    with open(fileName, 'r') as inFile:
        rawWords = inFile.read().split('\n')
    # Prep every words and put it in dictionary 
    words = {}
    for rawWord in rawWords:
        for word in prepWords(rawWord):
            key = getType(word)
            if key not in words:
                words[key] = []
            words[key] += [word]
    # Remove duplicates
    for key in words:
        words[key] = set(words[key])
    # Finishing touch
    print(sum(len(words[key]) for key in words), 'words loaded in', time.time() - t, 'seconds')
    return words


def orderedSet(lst):
    '''
    Does the same as set(x), but preserves order
    '''
    seen = {}
    result = []
    # Appends every item only if it's new
    for item in lst:
        if item in seen:
            continue
        seen[item] = None
        result.append(item)
    return result


def getType(word):
    '''
    Returns the type of word - it must be prepped (lowercase and only alpha)
    Example: radars -> abcbad
    '''
    setWord = ''.join(orderedSet(word))
    return word.translate(str.maketrans(setWord, alphabet[:len(setWord)]))


def freqSentence(words):
    '''
    Input: list of lowercase words, output dictionary with letters and their frequencies
    '''
    # Initialise dictionary
    freqs = {letter: 0 for letter in alphabet}
    totalLetters = 0
    # Count the letters in the words
    for word in words:
        for letter in word:
            freqs[letter] += 1
            totalLetters += 1
    # Return the frequencies (note that they are not normalised)
    return freqs


def sortFreq(d):
    '''
    Sort dictionary based on the frequencies into a list
    '''
    return sorted(d.items(), key=lambda x: x[1], reverse=True)


def matchFreqsRec(t1, t2, n, k, l=[]):
    '''
    Input: two lists of sortFreq, and two numbers n <= k (l is used internally)
    The first n elements of t1 are matched to the first k elements of t2
    '''

    for i in range(k):
        # If the number hasn't already been used
        if i not in l:
            # Add to dictionary of new matchFreqsRec call
            if len(l) < n - 1:
                a = matchFreqsRec(t1, t2, n, k, l + [i])
                for z in a:
                    z.update({t1[len(l)][0]: t2[i][0]})
                    yield z
            # In the final case, yield a dictionary
            else:
                yield {t1[n - 1][0]: t2[i][0]}


def checkPossibilities(string, poss, key):
    '''
    Return all possibilities of string given a key
    '''
    word = ''
    complete = True
    # Decode string
    for letter in string:
        try:
            word += key[letter]
        except:
            word += '.'
            complete = False
    # If the word's complete, just check with in
    if complete:
        if word in poss:
            return [word]
        return []
    # Otherwise, use a regex
    reWord = re.compile(word)
    return [l for l in poss if reWord.match(l)]


def decode(string, p=.95, n=3):
    '''
    Main function, decodes string, n is number of letters guessed based on frequency
    '''
    # Time it!
    t = time.time()
    # Prepare the input
    words = prepWords(string)
    posses = {word: wordList.get(getType(word), []) for word in words}
    # Get letter freqencies
    freqsInput = sortFreq(freqSentence(words))
    freqsTheo = sortFreq(realFreqs)
    # A little bit of verbosity
    print('Input freqencies:       ' + str(freqsInput))
    print('Theoretical freqencies: ' + str(freqsTheo))
    # Generate starting keys
    matchFound = False
    prevGuesses = []
    for k in range(n, 27):
        # Guess first n characters of string in increasing number of characters of realFreqs
        guesses = list(matchFreqsRec(freqsInput, freqsTheo, n, k))
        for key in guesses:
            if key in prevGuesses:
                # Don't do anything double
                continue
            # See, something is happening!
            # print(key)
            # Fill in the rest of the letters
            for subkey in exhaust(words[:], posses.copy(), key):
                # If it (kind of) matches our string...
                if goodPercentage(words, posses, subkey) >= p:
                    # ... we print it!
                    print(deencrypt(alphabet, reverseDict(subkey)), '=>', deencrypt(string, subkey))
                    matchFound = True
            # If the key matched actual words, we're happy enough (unindent once or twice for more accuracy)
            if matchFound:
                print('Done in', time.time() - t, 'seconds')
                return
        prevGuesses = guesses
    # Well, this shouldn't happen
    print('Something, somewhere, went horribly wrong (no decoding found)')


def exhaust(toAnalyse, poss, key, prefix=''):
    '''
    Find all the possibilities given a certain key
    '''
    prefix += '    '
    oldToAnalyse = []
    bestWord = ''
    bestPos = []
    bestLenPos = float('inf')
    # print(prefix, 'TA: ', toAnalyse)
    # Something has to change before we're happy
    while toAnalyse != oldToAnalyse:
        oldToAnalyse = toAnalyse[:]
        # For every word, check the number of possibilities
        for word in oldToAnalyse:
            possibilities = checkPossibilities(word, poss[word], key)
            lenp = len(possibilities)
            # Is it 0 or 1, it's useless (but may expand the key)
            if lenp == 1:
                # print(prefix, 'Word (1 pos): ', word)
                toAnalyse.remove(word)
                try:
                    key = expandKey(word, possibilities[0], key)
                except:
                    # No valid possibilities for this word
                    pass
            elif lenp == 0:
                # print(prefix, 'Word (0 pos): ', word)
                toAnalyse.remove(word)
            # Otherwise, we want the best word with the fewest possibilities for the nex step
            else:
                poss[word] = possibilities
                if lenp < bestLenPos:
                    bestWord = word
                    bestPos = possibilities
                    bestLenPos = lenp
    # print(prefix, 'second part, TA: ', toAnalyse)
    # print(prefix, 'Num pos > 1: ', bestWord)
    # This next step is expanding the key with this word and yielding all possible keys
    for p in bestPos:
        # print(prefix + '    ', p)
        try:
            newKey = expandKey(bestWord, p, key.copy())
            # print(prefix + '    ', 'newKey')
            for k in exhaust(toAnalyse[:], poss.copy(), newKey, prefix + '    '):
                yield k
        except:
            pass
    if len(toAnalyse) == 0:
        yield key


def goodPercentage(words, posses, key):
    '''
    Returns the percentage of words that are in the wordlist given a certain key
    '''
    # Get the translation dictionary for str.translate
    transKey = {ord(c): key.get(c, ' ') for c in alphabet}
    good = 0
    # Translate all words and see if they're in the dictionary
    for word in words:
        trans = word.translate(transKey)
        # If they have a character that's not in the key, they're not in the dictionary
        if ' ' in trans:
            continue
        if trans in posses[word]:
            good += 1
    # Normalise and return
    return good / len(words)


def expandKey(codedWord, realWord, key):
    '''
    Expand the key based on a word and what it corresponds to
    '''
    # Get the reverse dictionary for later
    revKey = reverseDict(key)
    for j in range(len(codedWord)):
        codedLetter = codedWord[j]
        realLetter = realWord[j]
        # The reverse key should not have a mismatch
        if revKey.get(realLetter, codedLetter) != codedLetter:
            break
        try:
            # Neither should the normal key
            if key[codedLetter] != realLetter:
                break
        except:
            # Hey, the letter from the coded word is missing from the key!
            key[codedLetter] = realLetter
    else:
        return key
    raise ValueError("Word doesn't fit with key")


def deencrypt(string, key):
    '''
    Return the string, deencrypted by the key
    '''
    w = ''
    # Iterate over the string, decode with key, retain weird symbols
    for letter in prepWord(string):
        w += key.get(letter, '_' if letter.isalpha() else letter)
    return w


# Please be careful with your input
def reverseDict(dict):
    '''
    Reverses a dictionary, fails if dictionary has a double value or non-hashable values
    '''
    return {y: x for x, y in dict.items()}


# Define the word list as a global variable
if 'wordList' not in globals():
    wordList = loadWordList()

# Do a test decoding
# if __name__ == '__main__':
#    decode('het is allemaal reusachtig treurig maar het is helaas niet anders, zo is het maar net', 2)
