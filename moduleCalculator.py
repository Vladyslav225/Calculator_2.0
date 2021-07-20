#Entering characters

def inputNumber(userNumber):

    while True:

        userNumber = input("Input number: ")

        if userNumber == "0":
            print("You can't use 0")
            continue

#Termial cleaning
        elif userNumber.lower() == "clear" or userNumber.lower() == "clean":
            print("\033c")
            continue

#Exit from module
        elif userNumber.lower() == "exit":    
            exit()

        elif userNumber == " " or userNumber == "":    
            print("Input number!!!")
            continue


        return float(userNumber)


############

#First User's number + Second User's number (First calculation)

def inputSymbol(operator):

    while True:

        try:

            print("You can use these operators: \nAdding: ' + '; \nSubtraction: ' - '; \nIncrease: ' * '; \nDivision: ' / ';")
            print("You can use these operators: \nInteger division of two numbers: ' // '; \nDegreeing: ' ** '; \nObtaining the balance of divdsion: ' % '")

            operator = input("Operator: ")
            return operator
        
        except:
            print("Input operator!!!")
            continue
##########

def resultUser(operator, firstNumber, secondNumber):

        if operator == "+":
            resultUser = round(firstNumber + secondNumber, 3)
            return resultUser
    
        # elif operator == "-":
        #     resultUser = round(firstNumber - secondNumber, 3)
        #     return resultUser

        # elif operator == "*":
        #     resultUser = round(firstNumber * secondNumber, 3)
        #     return resultUser
    
        # elif operator == "/":
        #     resultUser = round(firstNumber / secondNumber, 3)
        #     return resultUser

        # elif operator == "**":
        #     resultUser = round(firstNumber ** secondNumber, 3)
        #     return resultUser

        # elif operator == "//":
        #     resultUser = round(firstNumber // secondNumber, 3)
        #     return resultUser
    
        # elif operator == "%":
        #     resultUser = round(firstNumber % secondNumber, 3)
        #     return resultUser




##########

# def resultsUser(operator, firstNumber, secondNumber):

#         if operator == "+":
#             resultUser = round(firstNumber + secondNumber, 3)
#             return resultUser
    
        # elif operator == "-":
        #     resultUser = round(firstNumber - secondNumber, 3)
        #     return resultUser

        # elif operator == "*":
        #     resultUser = round(firstNumber * secondNumber, 3)
        #     return resultUser
    
        # elif operator == "/":
        #     resultUser = round(firstNumber / secondNumber, 3)
        #     return resultUser

        # elif operator == "**":
        #     resultUser = round(firstNumber ** secondNumber, 3)
        #     return resultUser

        # elif operator == "//":
        #     resultUser = round(firstNumber // secondNumber, 3)
        #     return resultUser
    
        # elif operator == "%":
        #     resultUser = round(firstNumber % secondNumber, 3)
        #     return resultUser
