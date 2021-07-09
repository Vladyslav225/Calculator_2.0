def inputNumber(userNumber):

    userNumber = input(": ")
    return float(userNumber)

############

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

###########

def inputSymbol1(operator, resultUser, userNumber3):
    operator = input("Operator: ")

    while True:

        if operator == "+":
            operator = round(resultUser + userNumber3, 3)
            return operator
        
        elif operator == "-":
            operator = round(resultUser + userNumber3, 3)
            return operator

        elif operator == "*":
            operator = round(resultUser + userNumber3, 3)
            return operator
        
        elif operator == "/":
            operator = round(resultUser + userNumber3, 3)
            return operator

        else:
            print("Input operator!!!")
            operator = input("Operator: ")
            continue
