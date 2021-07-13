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
        elif userNumber.lower() == "exit" or userNumber.lower() == "end":    
            exit()

        return float(userNumber)


############

#First User's number + Second User's number (First calculation)

def inputSymbol(operator, firstNumber, secondNumber, resultNumber):

    while True:

        operator = input("Operator: ")

        if operator == "+":
            resultNumber = firstNumber + secondNumber
            return resultNumber
    
        elif operator == "-":
            operator = round(firstNumber - secondNumber, 3)
            return operator

        elif operator == "*":
            operator = round(firstNumber * secondNumber, 3)
            return operator
    
        elif operator == "/":
            operator = round(firstNumber / secondNumber, 3)
            return operator

        elif operator == "**":
            operator = round(firstNumber ** secondNumber, 3)
            return operator

        elif operator == "//":
            operator = round(firstNumber // secondNumber, 3)
            return operator
    
        elif operator == "%":
            operator = round(firstNumber % secondNumber, 3)
            return operator

        else:
            print("Input operator!!!")
            continue

##########

#First calculation + Third User's number (Second calculation)

def inputSymbol1(operator, first_resultUser, thirdNumber):

    while True:

        operator = input("Operator: ")

        if operator == "+":
            operator = round(first_resultUser + thirdNumber, 3)
            return operator
        
        elif operator == "-":
            operator = round(first_resultUser - thirdNumber, 3)
            return operator

        elif operator == "*":
            operator = round(first_resultUser * thirdNumber, 3)
            return operator
        
        elif operator == "/":
            operator = round(first_resultUser / thirdNumber, 3)
            return operator

        elif operator == "**":
            operator = round(first_resultUser ** thirdNumber, 3)
            return operator

        elif operator == "//":
            operator = round(first_resultUser // thirdNumber, 3)
            return operator
        
        elif operator == "%":
            operator = round(first_resultUser % thirdNumber, 3)
            return operator

        else:
            print("Input operator!!!")
            continue
