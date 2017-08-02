#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint

def takeRamdomWords(strText, quantWords):
    """The takeRamdomWords function The text itself and the number of words are removed from it

    @:parameter strText String representing the text itself
    @:parameter quantWords Number of words that will be replaced by something like
    ___% d___ (%d being an integer)
    @:return List of strings that are the words that have been substituted
    of the text, and also the text itself with the words replaced
    by ___% d___ (% d being an integer)"""

    copyStrText = stringToListString(strText)
    ramdomWordsList, numGenerates = [], []
    i = 0
    illegalWords = ["\n", '\ufeff', "", " "]
    while i != quantWords:
        ramdNum = randint(0,len(copyStrText)-1)
        ramdomWord = copyStrText[ramdNum]
        if(ramdomWord not in illegalWords) and numbersInSequence(numGenerates, ramdNum):
            numGenerates.append(ramdNum)
            ramdomWordsList.append(ramdomWord)
            copyStrText = replaceWords(ramdomWord, wordBlank(i), copyStrText)
            illegalWords.append(wordBlank(i))
            i +=1
    return ramdomWordsList, retornToString(copyStrText, strText)

def wordBlank(index):
    """The wordBlank function Returns a string in the format ___% d___ (%d being an integer),
    which will be the word to replace the words taken at random

    @:return a string that will replace the words chosen in the text"""

    return "___"+str(index+1)+"___"

def numbersInSequence(listaNum, num):
    """The numbersInSequence function Analyzes whether there
    is no predecessor or successor number to the randomly generated number.

    @:parameter listaNum, List of numbers already generated
    @:parameter num, Last number generated
    @:return True if the list does not contain a predecessor
    or successor value to the value passed as a parameter in the function
    Otherwise false"""

    state = True
    if (num + 1) in listaNum or (num - 1) in listaNum:
        state = False
    return state

def stringToListString(strText, dot_comma = True):
    """The stringToListString function takes two arguments and does the String slicing without commas
    and points if dot_comma is true, if dot_comma is false the slicing is done with dots and commas

    @:parameter strText, Type string representing the text to be sliced
    @:parameter dot_commaBoolean, type, if true the dots and commas will
    be taken from the text otherwise
    @:return a list of strings"""

    spaceOnSplit = " "
    copyStrText = strText
    if dot_comma:
        dotOnReplace = "."
        commaOnReplace = ","
        copyStrText = copyStrText.replace(dotOnReplace,"")
        copyStrText = copyStrText.replace(commaOnReplace,"")
    copyStrText = copyStrText.split(spaceOnSplit)
    return copyStrText

def replaceWords(word, substituteWord, listText):
    """the replaceWords function receives three arguments and replaces
    all values equal to the first argument in listText by the second.

    @:parameter word, Searched word in the list and will be replaced
    @:parameter substituteWord, Word that will replace all that are equal to word
    @:parameter listText, A vector of strings representing the original text
    @:return A vector where the necessary substitutions were made"""

    for i in range(len(listText)):
        if listText[i] == word:
            listText[i] = substituteWord
    return  listText

def retornToString(listText, originalText):
    """The returnToString function takes two arguments a vector of strings and a string
    By recreating a new string from the two arguments passed.

    @:parameter listaText A vector of strings representing the original text
    @:parameter originalText Original text a unique String
    @:return A string recipe from the string vector(listText) and the original text (originalText)"""

    strText = ""
    spaceOnWords = " "
    originalTextList = stringToListString(originalText,False)
    for i in range(len(listText)):
        try:
            if originalTextList[i][:-1] == listText[i]:
                strText += originalTextList[i]+spaceOnWords
            else:
                strText += listText[i]+spaceOnWords
        except: continue
    return strText

def gameText():
    '''Returns a string that is text without changes

    @:return a string that is text for the game'''

    textOrigin = "Não acredite em algo simplesmente porque ouviu. Não acredite em algo\n"\
                 "simplesmente porque todos falam a respeito. Não acredite em algo simplesmente\n"\
                 "porque está escrito em seus livros religiosos. Não acredite em algo só porque seus\n"\
                 "professores e mestres dizem que é verdade. Não acredite em tradições só porque\n"\
                 "foram passadas de geração em geração. Mas depois de muita análise e\n"\
                 "observação, se você vê que algo concorda com a razão, e que conduz ao bem e\n"\
                 "beneficio de todos, aceite-o e viva-o."
    return textOrigin

def endGame(wordsRamdomList, strText):
    '''The endGame function Verifies that the game has come to an end, that is, the player has
    been able to guess all the words Receiving two arguments the list of random words taken from the text
     and the text itself

    @:parameter wordsRamdomList, List of random words that were taken from the text
    @:parameter strText, The text itself without changes
    @:return True if the player was able to guess all the words, or false if he still has not left words'''

    state = True
    for i in range(len(wordsRamdomList)):
        blank = "___"+str(i+1)+"___"
        if strText.count(blank) != 0:
            state = False
    return state

def inputLevelGame():
    """The function receives the user a valid level (easy, medium, hard)
    and returns a list of words that have been removed and the text after these words are removed

    @:return List of words taken and the text after removing the words from the list"""

    levelsGame = {"EASY": 4, "MEDIUM": 7, "HARD": 9}
    while True:
        levelGame = input("Choose the level of the game:\nEasy\nMedium\nHard\n").upper()
        try:
            wordsBlank, strText = takeRamdomWords(gameText(), levelsGame[levelGame])
            break
        except:
            print("Invalid option try again: \n")
            continue
    print(strText)
    return wordsBlank, strText

def main():
    """the main function, Main function where the game is executed, does not r
    eceive arguments and has no return"""

    counter = 0
    wordsBlank, strText = inputLevelGame()
    while endGame(wordsBlank, strText) is not True:
        print("what should go in blank number ", counter+1,"?")
        searchWord = input()
        if searchWord == wordsBlank[counter]:
            copyStrText = replaceWords(wordBlank(counter),searchWord, stringToListString(strText))
            strText = retornToString(copyStrText, gameText())
            counter +=1
            print("\n",strText,"\n")
        else: print("Ops!!! This is not the word number ",counter+1," try again!!!")
    print("Game Win!!!!")

#Start of execution
main()