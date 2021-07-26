allOperator = ["+", "-", "*", "/", "**", "//", "%"]


def inputNumber(userNumber):

    while True:

        userNumber = input("Input number: ")

        if userNumber.lower() == "exit":
            exit()

        elif userNumber.lower() == "clear":
            print("\033c")

        elif userNumber == "0":
            print("You can't use 0")
            continue

        try:
            return float(userNumber)

        except ValueError:
            print("Input Number!!!")
            continue


def inputOperator(operator):
    
    while True:

        print("Choose an operator", allOperator)

        operator = input("Input operator: ")

        if operator.lower() == "exit":
            exit()

        elif operator.lower() == "clear":
            print("\033c")

        try:
            if operator in allOperator:
                return operator

        except ValueError:
            print("ValueError")
            continue


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