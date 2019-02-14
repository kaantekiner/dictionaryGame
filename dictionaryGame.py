import random
import sys

## Varaibles For Use During Gameplay
QuestionCountPerLevel = 5  ## Dynamic option for asking questions, you can change how many questions game will ask per level.
OperatorsForUse = ["+","-","*","/","%"]
MaxValueOfQuestionNumberDigit = 15  ## Dynamic option for questions, you can change which number will be maximum of questions digits. This can be also used for setting game easy or hard.
UsersStarCount = 0  ## How many stars user have. Please don't make a change, so player will be start with 0 stars.
UsersTotalErrorCount = 0  ## How many mistakes user have during all game. Please don't make a change, so player will be start with 0 mistake.
AnswerOfCurrentQuestion = 0

def BuildLevelsAndQuestions(Level):
    for i in range(1, QuestionCountPerLevel + 1):  ## Building questions for current level with for loop
        print("\n")
        Number1 = random.randint(1, MaxValueOfQuestionNumberDigit)  ## Randomly selecting 2 numbers for use in question
        Number2 = random.randint(1, MaxValueOfQuestionNumberDigit)
        SelectedOperatorIndex = random.randint(0, Level - 1)
        SelectedOperator = OperatorsForUse[
            SelectedOperatorIndex]  ## Selecting operator randomly which can be usable for current level
        Question = str(Number1) + " " + str(SelectedOperator) + " " + str(Number2)  ## Make a question string
        global AnswerOfCurrentQuestion
        AnswerOfCurrentQuestion = 0
        if SelectedOperator == OperatorsForUse[0]:  ## Determining the mathematically calculating progress of answer.
            AnswerOfCurrentQuestion = Number1 + Number2
        if SelectedOperator == OperatorsForUse[1]:
            AnswerOfCurrentQuestion = Number1 - Number2
        if SelectedOperator == OperatorsForUse[2]:
            AnswerOfCurrentQuestion = Number1 * Number2
        if SelectedOperator == OperatorsForUse[3]:
            AnswerOfCurrentQuestion = Number1 / Number2
        if SelectedOperator == OperatorsForUse[4]:
            AnswerOfCurrentQuestion = Number1 % Number2
        ## Asking question
        print("Question " + str(i), "Level " + str(Level))
        print("\n")
        print(Question)
        print(">>>")
        TakeInputFromUserAndControl(AnswerOfCurrentQuestion)  ## Time to control type of users input
def TakeInputFromUserAndControl(AnswerOfCurrentQuestion): ## BONUS PART
    global UsersStarCount
    global UsersTotalErrorCount
    AnswerOfCurrentQuestionFromInput = input()  ## Take input from user
    IsInputInt = False
    try:   ## Try to make it an integer
        val = int(AnswerOfCurrentQuestionFromInput)
        IsInputInt = True
    except ValueError:   ## If can't
        IsInputInt = False   ## Says its not an integer
    if IsInputInt:   ## If it is an integer
        AnswerOfCurrentQuestionFromInput = int(AnswerOfCurrentQuestionFromInput)   ## Convert the string-based input value to an integer for progress
        if AnswerOfCurrentQuestionFromInput == AnswerOfCurrentQuestion:   ## Controlling correction of solution and users answer
            UsersStarCount = UsersStarCount + 1   ## Give stars to correct answer
            print("\n")
            print("Correct! You gain an additional star! You now have " + str(UsersStarCount) + " out of " + str(
                QuestionCountPerLevel) + " stars!")
        else:   ## If users answer is wrong, say it and increase UsersTotalErrorCount
            print("\n")
            print("Wrong! You do not gain any stars for that question! You still have " + str(
                UsersStarCount) + " out of " + str(QuestionCountPerLevel) + " stars!")
            UsersTotalErrorCount = UsersTotalErrorCount + 1
    else:    ## If users input is not an integer make warning
        print("ERROR! Un-acceptable entry detected, try again please!")
        TakeInputFromUserAndControl(AnswerOfCurrentQuestion)  ## And call method again to restart this progres
def StartGame():
    print("\n")
    print("\n")
    print("Welcome To MathMini!")   ## Welcome user
    print("____________________")
    print("\n")
    print("Now, you will get some information abouth your level and gameplay. After, your questions will be asked one by one.")
    print("\n")
    ## Make the warning of integer-float thing. The reason is that why we doing this (and converting answers to integer all the time is because the conculusion of 3/7 = 0.42857142857.
    #  Player will not want to type this, so he can easily cut the part which comes after dot(.) or comma(,) and type it. Answer will be accepted)
    print("IMPORTANT! All the answers will be type of integer: If an solution of a question is type of float or etc., " + "\n" +
          "program will automatically convert it to an integer. So; if the question is 3/2; You should" + "\n" +
          "NOT type 1.5, you should type 1 because of converting an float or double to integer means" + "\n" + "just taking the part of number which is before coma or dot.")
    print("\n")
    for Level in range(1, 6):  ## Dynamically building levels with for loop
        print("\n")
        print("Your Level Is " + str(Level))
        print("Possible length of Numbers: " + str(len(str(MaxValueOfQuestionNumberDigit))))   ## Calculating possible lenght of digits which will be use in questions
        print("Possible number of Operators: " + str(Level))   ## Calculating the operator count which will user progress with in current level
        BuildLevelsAndQuestions(Level)
        print("\n")
        print("Level " + str(Level) + " Finish!")   ## When level finish, says to user
        global UsersStarCount
        if UsersStarCount >= 3:   ## If user have enough stars to pass other level
            print("You have enough stars this level, time to move on!")
            UsersStarCount = 0   ## Make star count zero because of starting a new level
            if Level == 5:   ## If user finishes last level which is 5, says game beaten and how many mistakes user has during all game
                print("Amazing! You beat the game! You answered a total of " + str(UsersTotalErrorCount) + " answers wrong this attempt. You can press any key to quit.")
                input("Press Enter key to say goodbye!")
                sys.exit()  ## Exit game clearly
        else:
            print("\n")  ## If user don't have enough star, says game will end, goodby and how many mistakes user has during all game.
            print("You do not have enough stars to move on to the next level, this as far as you go!")
            print("Your total mistake count is = " + str(UsersTotalErrorCount) + ", Goodbye...")
            input("Press Enter key to say goodbye!")
            sys.exit()   ## Exit game clearly
StartGame()   ## Start the game by calling function.

