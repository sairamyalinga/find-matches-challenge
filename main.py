import re
import sys
from tabulate import tabulate

wordCount = {}
wordSet = set()
nonAlphanumericRegex = re.compile(r"^\W+|\W+$")


def readPredefinedWords(predefinedWordsFile):
    try:
        with open(predefinedWordsFile, 'r') as file:
            for line in file:
                word = line.strip()
                wordSet.add(word)
                wordCount[word.lower()] = 0
    except Exception as err:
        print(err)
        exit(1)


def processLine(line):
    words = line.split(" ")
    for word in words:
        word = nonAlphanumericRegex.sub("", word)
        word = word.lower()
        if word in wordCount:
            wordCount[word] += 1


def processInputFile(fileName):
    try:
        with open(fileName, 'r') as file:
            for line in file:
                processLine(line)
    except Exception as err:
        print(err)
        exit(1)


readPredefinedWords(sys.argv[1])
processInputFile(sys.argv[2])
sortedWordSet = sorted(wordSet, key=lambda x: wordCount[x.lower()], reverse=True)
output = []
for word in sortedWordSet:
    if wordCount[word.lower()] == 0:
        break
    output.append([word, wordCount[word.lower()]])

print(tabulate(output, headers=['Predefined word', 'Match count'], tablefmt="simple_grid"))
