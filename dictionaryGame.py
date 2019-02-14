import random
import sys

## Varaibles For Use During Gameplay

## Word List
WordList = ["black","car","plane","cat","sea","ocean","fruit","food","directory","blabla"]
## Defination List
WordDefinations = ["Having the darkest colour there is, like the colour of a very dark night.",
            "A road vehicle with an engine.",
            "A vehicle designed for air travel.",
            "A small animal with fur, four legs, a tail, and claws.",
            "The salty water that covers a large part of the surface of the earth.",
            "A very large sea area.",
            "The soft part containing seeds that is produced by a plant.",
            "Something that people and animals eat to keep them alive.",
            "A book that gives a list of names, addresses, or other facts.",
            "yyyyblayyyy"]
Dictionary = []
global LastSearchedInput
global LastRecommendList
def StartGame():
    print ("")
    print ("Welcome to the Dictionary Game")
    print ("")
    print ("INFORMATION")
    print ("You already have " + str(len(WordList)) + " word with their definations.")
    BuildDictionary(WordList,WordDefinations)
def BuildDictionary(WordList,WordDefinations):
    print ("")
    print ("Building Dictionary...")
    for i in range(len(WordList)):
        Dictionary.append(WordList[i])
        Dictionary.append(WordDefinations[i])
    print("Dictionary Built!")
    print ("")
    ShowMainOptions()
def ShowMainOptions():
    global LastRecommendList
    global LastSearchedInput
    LastRecommendList = []
    LastSearchedInput = ""
    print("Please select one of these options:")
    print("1. Add a new word")
    print("2. Update an existing word")
    print("3. Delete an existing word")
    print("4. Display a word's definition")
    UsersSelectedOption = raw_input(">>>")
    if UsersSelectedOption == "1" or UsersSelectedOption == "2" or UsersSelectedOption == "3" or UsersSelectedOption == "4":
        if UsersSelectedOption == "1":
            AddDefination()
        if UsersSelectedOption == "2":
            UpdateDefination()
        if UsersSelectedOption == "3":
            DeleteDefination()
        if UsersSelectedOption == "4":
            DisplayDefination()
    else:
        print ("You type a wrong option, please try again:")
        ShowMainOptions()
def AddDefination():
    print("What word do you want to add?")
    Input = raw_input(">>>")
    print("Please add in a definition for this word(" + Input + "):")
    InputDefination = raw_input(">>>")
    Dictionary.append(Input)
    Dictionary.append(InputDefination)
    print(Input + " added in correctly!")
    print("")
    ContinueOrNot()
def UpdateDefination():
    global IndexOfInput
    print("What word do you want to update?")
    Input = raw_input(">>>")
    IsFounded = False
    for i in range(len(Dictionary)):
        if Input == Dictionary[i]:
            IndexOfInput = i
            IsFounded = True
            break
    if IsFounded:
        ContiuneUpdate(IndexOfInput)
    else:
        CannotFoundWordUpdate()
def ContiuneUpdate(IndexOfInput):
    print("Please write in a new definition" + "(" +Dictionary[IndexOfInput] + "):")
    InputDefination = raw_input(">>>")
    Dictionary[IndexOfInput + 1] = InputDefination
    print(Dictionary[IndexOfInput] + " was updated correctly!")
    print("")
    ContinueOrNot()
def CannotFoundWordUpdate():
    print("Error the word is not in the dictionary! You may perform these actions:")
    print("1. Retry with another word.")
    print("2, Return to main menu")
    Desicion = raw_input(">>>")
    if Desicion == "1" or Desicion == "2":
        if Desicion == "1":
            UpdateDefination()
        if Desicion == "2":
            ShowMainOptions()
    else:
        print ("You type a wrong option, please try again:")
        CannotFoundWordUpdate()
def DeleteDefination():
    global IndexOfInput
    print("What word do you want to delete?")
    Input = raw_input(">>>")
    IsFounded = False
    for i in range(len(Dictionary)):
        if Input == Dictionary[i]:
            IndexOfInput = i
            IsFounded = True
            break
    if IsFounded:
        ContiuneDelete(IndexOfInput)
    else:
        CannotFoundWordDelete()
def ContiuneDelete(IndexOfInput):
    Word = Dictionary[IndexOfInput]
    Dictionary.pop(IndexOfInput)
    Dictionary.pop(IndexOfInput)
    print(Word + " and its defination was deleted correctly!")
    print("")
    for i in range(len(Dictionary)):
        print(Dictionary[i])
    ContinueOrNot()
def CannotFoundWordDelete():
    print("Error the word is not in the dictionary! You may perform these actions:")
    print("1. Retry with another word.")
    print("2, Return to main menu")
    Desicion = raw_input(">>>")
    if Desicion == "1" or Desicion == "2":
        if Desicion == "1":
            DeleteDefination()
        if Desicion == "2":
            ShowMainOptions()
    else:
        print ("You type a wrong option, please try again:")
        CannotFoundWordDelete()
def DisplayDefination():
    global IndexOfInput
    print("Please enter a search term:")
    Input = raw_input(">>>")
    global LastSearchedInput
    LastSearchedInput = Input
    IsFounded = False
    for i in range(len(Dictionary)):
        if Input == Dictionary[i]:
            IndexOfInput = i
            IsFounded = True
            break
    if IsFounded:
        DisplayDefinationOfInput(IndexOfInput)
    else:
        SearchForSubtring(Input)
def SearchForSubtring(Input):
    global LastRecommendList
    global RecommendList
    RecommendList = []
    LastRecommendList = []
    for a in range(0,len(Dictionary),2):
        if Dictionary[a].__contains__(Input):
            RecommendList.append(Dictionary[a])
    if len(RecommendList) > 0:
        print ("Here are all the words that match the search term, please choose that word you want:")
        LastRecommendList = RecommendList
        ShowMatches(RecommendList)
    else:
        NoMatchError()
def ShowMatches(RecommendList):
    OptionNumberList = []
    for i in range(len(RecommendList)):
        print(str(i + 1) + ":" + " " + RecommendList[i])
        OptionNumberList.append(i+1)
    UserSelectBestMatches(OptionNumberList)
def UserSelectBestMatches(OptionNumberList):
    Desicion = raw_input(">>>")
    Contains = False
    KelimeninIndexi = 0
    for i in range(len(OptionNumberList)):
        if Desicion == str(OptionNumberList[i]):
            KelimeninIndexi = OptionNumberList[i]
            Contains = True
            break
    if Contains:
        WordToDisplay = LastRecommendList[KelimeninIndexi-1]
        IndexOfWordToDisplay = Dictionary.index(WordToDisplay)
        DisplayDefinationOfInput(IndexOfWordToDisplay)
    else:
        print ("You type a wrong match number, please try again:")
        SearchForSubtring(LastSearchedInput)
def NoMatchError():
    print("Error no word matches this search term, theese are some options you can select;")
    print("1.Try with a new search term")
    print("2.Continue to main menu")
    print("3.Exit Game")
    Desicion = raw_input(">>>")
    if Desicion == "1" or Desicion == "2" or Desicion == "3":
        if Desicion == "1":
            DisplayDefination()
        if Desicion == "2":
            ShowMainOptions()
        if Desicion == "3":
            print ("Goodbye!")
            sys.exit(0)
    else:
        print ("You type a wrong option, please try again:")
        NoMatchError()
def DisplayDefinationOfInput(IndexOfInput):
    print(Dictionary[IndexOfInput]+":"+" "+Dictionary[IndexOfInput+1])
    ContinueOrNot()
def ContinueOrNot():
    print("Would you like to continue or exit?")
    print("1.Continue")
    print("2.Exit")
    Desicion = raw_input(">>>")
    if Desicion == "1" or Desicion == "2":
        if Desicion == "1":
            ShowMainOptions()
        if Desicion == "2":
            print ("Goodbye!")
            sys.exit(0)
    else:
        print ("You type a wrong option, please try again:")
        ContinueOrNot()
StartGame()

