import random

wordList = [
    "alien invasion", 
    "Temple of Doom", 
    "Bermuda Triangle", 
    "howling", 
    "knocking",
    "bump in the night", 
    "hockey mask", 
    "full moon"
]
index = 0
random.shuffle(wordList)

def moveIndex(wordList, index):
    if index == len(wordList) - 1:
        index = 0
    else:
        index += 1
    return index


def changeHiddenWord(hiddenWord, word, letter):
    newHiddenWord = ""
    for i in range(0, len(hiddenWord)):
        if word[i].lower() == letter.lower():
            newHiddenWord += word[i]
        else:
            newHiddenWord += hiddenWord[i]
    return newHiddenWord

def hideWord(word):
    hiddenWord = ""
    for c in word:
        if c.isalpha():
            hiddenWord += '-'
        else:
            hiddenWord += c
    return hiddenWord

def startGame(word):
    hiddenWord = hideWord(word)

    print(hiddenWord)
    while hiddenWord != word:
        letter = input("Enter letter")
        hiddenWord = changeHiddenWord(hiddenWord, word, letter)
        print(hiddenWord)


while True:
    play = input("Would you like to play hangman? ")
    if play == 'yes' or play == 'y':
        word = wordList[index]
        index = moveIndex(wordList, index)
        startGame(word)
    elif play == 'no' or play == 'n':
        break