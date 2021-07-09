import moduleCalculator as mcal     #Подключение модуля


#Знакомство программы с переменными
resultUser = " "
userNumber = " "
operator = " "
userNumber1 = " "
userNumber2 = " "


while True:
    try:
        userNumber1 = mcal.inputNumber(userNumber)  #Первое число
        print(userNumber1)

        userNumber2 = mcal.inputNumber(userNumber)  #Второе число
        print(userNumber2)

        resultUser = mcal.inputSymbol(operator, userNumber1, userNumber2)   #Обращение к расчету первых двух чисел (Первый расчет)
        print(resultUser)

        userNumber3 = mcal.inputNumber(userNumber)  #Третье число
        print(userNumber3)

        resultUser1 = mcal.inputSymbol1(operator, resultUser, userNumber3)  #Обращение к расчету с третьим числом
        print(resultUser1)

    except:
        print("Input number!!!")
        continue
    
    #inputSymbol(operator, userNumber1, userNumber2)
    # mcal.inputNumber(userNumber)
    # mcal.inputNumber(userNumber)