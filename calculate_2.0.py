import moduleCalculator as mcal



resultUser = " "
userNumber = " "
operator = " "
userNumber1 = " "
userNumber2 = " "


while True:
    try:
        userNumber1 = mcal.inputNumber(userNumber)
        print(userNumber1)

        userNumber2 = mcal.inputNumber(userNumber)
        print(userNumber2)

        resultUser = mcal.inputSymbol(operator, userNumber1, userNumber2)
        print(resultUser)

        userNumber3 = mcal.inputNumber(userNumber)
        print(userNumber3)

        resultUser1 = mcal.inputSymbol1(operator, resultUser, userNumber3)
        print(resultUser1)

    except:
        print("Input number!!!")
        continue
    
    #inputSymbol(operator, userNumber1, userNumber2)
    # mcal.inputNumber(userNumber)
    # mcal.inputNumber(userNumber)