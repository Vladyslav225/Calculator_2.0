allOperator = ["+", "-", "*", "/", "**", "//", "%"]



def exit_clear(userNumber, operator):

    if userNumber.lower() == "exit" or operator.lower() == "exit":

        return exit()

    elif userNumber.lower() == "clear" or operator.lower() == "clear":

        return ("\033c")


        
def inputNumber(userNumber, operator):

    while True:

        userNumber = input("Input number: ")

        userNumber = exit_clear(userNumber, operator)

        if userNumber == "0":
            print("You can't use 0")
            continue

        try:
            return float(userNumber)

        except ValueError:
            print("Input Number!!!")


def inputOperator(userNumber, operator):
    
    while True:

        print("Choose an operator", allOperator)

        operator = input("Input operator: ")

        operator = exit_clear(userNumber, operator)

        try:
            if operator in allOperator:
                return operator

        except ValueError:
            print("ValueError")


def calculation(firstNumber, secondNumber, operator):

    if operator == "+":
        result = firstNumber + secondNumber
        return round(result, 3)

    elif operator == "-":
        result = firstNumber - secondNumber
        return round(result, 3)

    elif operator == "*":
        result = firstNumber * secondNumber
        return round(result, 3)

    elif operator == "/":
        result = firstNumber / secondNumber
        return round(result, 3)

    elif operator == "**":
        result = firstNumber ** secondNumber
        return round(result, 3)

    elif operator == "//":
        result = firstNumber ** secondNumber
        return round(result, 3)

    elif operator == "%":
        result = firstNumber % secondNumber
        return round(result, 3)

