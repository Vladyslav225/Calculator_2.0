#Entering characters

def inputNumber(userNumber):

    userNumber = input("Input number: ")

#Exit from module
    if userNumber.lower() == "exit":    
        exit()

    return float(userNumber)


############

#First User's number + Second User's number (First calculation)

def inputSymbol(operator, userNumber1, userNumber2):
    operator = input("Operator: ")

    while True:

        if operator == "+":
            operator = round(userNumber1 + userNumber2, 3)
            return operator
    
        elif operator == "-":
            operator = round(userNumber1 - userNumber2, 3)
            return operator

        elif operator == "*":
            operator = round(userNumber1 * userNumber2, 3)
            return operator
    
        elif operator == "/":
            operator = round(userNumber1 / userNumber2, 3)
            return operator

        else:
            print("Input operator!!!")
            operator = input("Operator: ")
            continue

# ###########

#First calculation + Third User's number (Second calculation)

def inputSymbol1(operator, resultUser, userNumber3):
    operator = input("Operator: ")

    while True:

        if operator == "+":
            operator = round(resultUser + userNumber3, 3)
            return operator
        
        elif operator == "-":
            operator = round(resultUser - userNumber3, 3)
            return operator

        elif operator == "*":
            operator = round(resultUser * userNumber3, 3)
            return operator
        
        elif operator == "/":
            operator = round(resultUser / userNumber3, 3)
            return operator

        else:
            print("Input operator!!!")
            operator = input("Operator: ")
            continue
