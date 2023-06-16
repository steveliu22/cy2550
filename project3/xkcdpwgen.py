import sys
import random

def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print(''.join(generateRandomWords(4)))

    

def parseArgs(argNum):
    arg = argNum[0]
    num = argNum[1]

    if num == None or num < 0:
        num = 0

    match arg:
        case "-h":
            return "hi"
        case "-w":
            return "hi"
        case "-c":
            return "hi"
        case "-n":
            return "hi"
        case "-s":
            return "hi"
        case _:
            return "Invalid argument provided: " + arg
        


def addSymbolsToPassword(pwd, numOfSymbols):
    validSymbols = "~!@#$%^&*.:;"
    newPwd = pwd
    for i in range(numOfSymbols):
        nextSymbol = validSymbols[random.randint(len(validSymbols))]
        position = random.randint(len(newPwd))
        newPwd = addCharactersToString(newPwd, nextSymbol, position)

    return newPwd

def addNumbersToPassword(pwd, numOfNumbers):
    newPwd = pwd
    for i in range(numOfNumbers):
        nextNum = random.randint(0, 10)
        position = random.randint(len(newPwd))
        newPwd = addCharactersToString(newPwd, str(nextNum), position)

    return newPwd

def generateRandomWords(numWords):
    files = open('words.txt', 'r')
    words = files.readlines()
    numOfWords = len(words)
    
    randomWords = []

    for i in range(numWords):
        nextWord = words[random.randint(0, numOfWords)].strip()
        randomWords.append(nextWord)
    
    files.close()

    return randomWords

def addCharactersToString(string, newCharacter, position):
    if position > len(string) -1:
        position = len(string) - 1
    
    if position < 0:
        position = 0

    return string[:position] + newCharacter + string[position:]
    
if __name__ == "__main__":
    main()    

