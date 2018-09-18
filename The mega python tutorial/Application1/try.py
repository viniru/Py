import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def getMeaning(word):
    word = word.lower()
    if word in data:
        printMean(data.get(word))
    elif word.title() in data:
        printMean(data.get(word.upper()))
    elif word.upper() in data:
        printMean(data.get(word.upper()))
    else:
        match = get_close_matches(word,data.keys())
        if len(match) > 0:
            choice = input("Do you mean the word  %s  , y or n " % match[0])
            if choice == "y":
                printMean((data.get(match[0])))
            elif choice == "n":
                printMean(["No such word exists"])
            else:
                printMean(["We did not understand your response"])
        else:
            printMean(["No such word exists"])

def printMean(strings):
    for str in strings:
        print(str)

cont = "true";
while cont == "true" :
    word = input("Enter the word you want to search for : ")
    getMeaning(word)
    cont=input("Do you want to continue : ")
