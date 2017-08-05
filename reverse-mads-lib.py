#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint

def takeRamdomWords(strText, quantWords):
    """
        Behavior: It randomly selects a set of words and then substitutes
    all that are equal by a_ __%d___ (%d integer) of the same value.
        Input: The text that will be manipulated and the number of words that will be removed.
        Output: List with the words that were randomly taken, with no repetition and
    a string already with the appropriate blanks.
    """
    copyStrText = stringToListString(strText)
    ramdomWordsList, numGenerates = [], []
    iterador = 0
    illegalWords = ["\n", '\ufeff', "", " "]
    while iterador != quantWords:
        ramdNum = randint(0,len(copyStrText)-1)
        ramdomWord = copyStrText[ramdNum]
        if(ramdomWord not in illegalWords) and numbersInSequence(numGenerates, ramdNum):
            numGenerates.append(ramdNum)
            ramdomWordsList.append(ramdomWord)
            copyStrText = replaceWords(ramdomWord, wordBlank(iterador), copyStrText)
            illegalWords.append(wordBlank(iterador))
            iterador +=1
    return ramdomWordsList, retornToString(copyStrText, strText)

def wordBlank(index):
    """
        Behavior: Returns a string in the format ___% d___ (%d being an integer),
    which will be the word to replace the words taken at random.
        Input: The number of the blank.
        Output: A string that will replace the words chosen in the text.
    """

    return "___"+str(index+1)+"___"

def numbersInSequence(listaNum, num):
    """
        Behavior: Analyzes whether there is no predecessor or successor
    number to the randomly generated number.
        Input: A list of numbers already generated and the last number generated.
        Output: True if the list does not contain a predecessor
    or successor value to the value passed as a parameter in the function
    Otherwise false
    """

    state = True
    if (num + 1) in listaNum or (num - 1) in listaNum:
        state = False
    return state

def stringToListString(strText, dot_comma = True):
    """
        Behavior: Does the String slicing without commas
    and points if dot_comma is true, if dot_comma is false the slicing is done with dots and commas.
        Input: A string representing the text to be sliced and a boolean if true the dots and
    commas will be taken from the text, otherwise not.
        Output: A list containing all words in the string as its elements.
        """

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
    """
        Behavior: replaces all values equal to the first argument in listText by the second.
        Input: Searched word in the list and will be replaced with word that will replace all
    that are equal to word and a vector of strings representing the original text.
        Output: A vector where the necessary substitutions were made.
    """

    for index in range(len(listText)):
        if listText[index] == word:
            listText[index] = substituteWord
    return  listText

def retornToString(listText, originalText):
    """
        Behavior: Create a string with the elements of the list
    received by based on whether the string also received as a parameter.
        Input: A vector of strings representing the original text and
    Original text a unique String.
        Output: A string recipe from the string vector(listText) and the original text (originalText).
    """

    strText = ""
    spaceOnWords = " "
    originalTextList = stringToListString(originalText,False)
    for index in range(len(listText)):
        try:
            if originalTextList[index][:-1] == listText[index]:
                strText += originalTextList[index]+spaceOnWords
            else:
                strText += listText[index]+spaceOnWords
        except: continue
    return strText

def gameText():
    """
        Behavior: returns a string that is text without changes.
        Output: a string that is text for the game
    """
    textOrigin = "Não acredite em algo simplesmente porque ouviu. Não acredite em algo\n"\
                 "simplesmente porque todos falam a respeito. Não acredite em algo simplesmente\n"\
                 "porque está escrito em seus livros religiosos. Não acredite em algo só porque seus\n"\
                 "professores e mestres dizem que é verdade. Não acredite em tradições só porque\n"\
                 "foram passadas de geração em geração. Mas depois de muita análise e\n"\
                 "observação, se você vê que algo concorda com a razão, e que conduz ao bem e\n"\
                 "beneficio de todos, aceite-o e viva-o."
    return textOrigin

def endGame(wordsRamdomList, strText):
    """
        Behavior: Verifies that the game has come to an end, that is, the player has
    been able to guess all the words Receiving two arguments the list of random words taken from the text
    and the text itself.
        Input: List of random words that were taken from the text and The text itself without changes.
        Output: True if the player was able to guess all the words, or false if he still has not left words
    """

    state = True
    for numberWord in range(1, len(wordsRamdomList)+1):
        blank = "___"+str(numberWord)+"___"
        if strText.count(blank):
            state = False
    return state

def inputLevelGame():
    """
        Behavior: receives the user a valid level (easy, medium, hard)
    and returns a list of words that have been removed and the text after these words are removed.
        Output: List of words taken and the text after removing the words from the list
    """

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
    """
        Behavior: Is the main function executing all other functions in a systematic
        way and according to the requirements without parameters or return.
    """

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
