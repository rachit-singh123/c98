from fileinput import filename
from unicodedata import name


def countWordsFromFile():
    fileName=input("enter the file name:")
    numberOfWords=0
    file=open(fileName,'r')
    for i in file:
        words=i.split()
        numberOfWords=numberOfWords+len(words)
    print("numberOfWords:")
    print(numberOfWords)
countWordsFromFile()