import re
import sys
from tabulate import tabulate

wordCount = {}
wordSet = set()
nonAlphanumericRegex = re.compile(r"^[\W_]+|[\W_]+$")

# Goes through each of the predefined words,
# adds them to a set (with given text case) as well as a counter dict (with lowercase keys)
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

# Helper method to process each line in the given input file
def processLine(line):
    words = line.split(" ")
    for word in words:
        word = nonAlphanumericRegex.sub("", word)
        word = word.lower()
        if word in wordCount:
            wordCount[word] += 1

# Helper method to read the given input file
def processInputFile(fileName):
    try:
        with open(fileName, 'r') as file:
            for line in file:
                processLine(line)
    except Exception as err:
        print(err)
        exit(1)

# The main entrypoint
def main():
    readPredefinedWords(sys.argv[1])
    processInputFile(sys.argv[2])
    sortedWordSet = sorted(wordSet, key=lambda x: wordCount[x.lower()], reverse=True)
    output = []
    for word in sortedWordSet:
        if wordCount[word.lower()] == 0:
            break
        output.append([word, wordCount[word.lower()]])

    tabulated = tabulate(output, headers=['Predefined word', 'Match count'], tablefmt="simple_grid")
    print(tabulated)
    
    output = open("output.txt", "w")
    output.write(tabulated)
    output.close()

if __name__ == '__main__':
    main()
