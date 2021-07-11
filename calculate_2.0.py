import moduleCalculator as mcal     #Connecting the module


while True:

    print("To finish calculation write 'Exit' ")
    print("You can use these operators: \nAdding: ' + '; \nSubtraction: ' - '; \nIncrease: ' * '; \nDivision: ' / ';")
    print("You can use these operators: \nInteger division of two numbers: ' // '; \nDegreeing: ' ** '; \nObtaining the balance of divdsion: ' % '")

#Acquaintance of the prgram with the variables used
    
    resultUser = " "
    userNumber = " "
    operator = " "
    userNumber1 = " "
    userNumber2 = " "

    
    try:

#Firrst User's number        
        userNumber1 = mcal.inputNumber(userNumber)  
        print(userNumber1)

#Second User's number        
        userNumber2 = mcal.inputNumber(userNumber)  
        print(userNumber2)

 #First User's number + Second User's number (First calculation)
        resultUser = mcal.inputSymbol(operator, userNumber1, userNumber2)  
        print(resultUser)

        
#Third User's number
        userNumber3 = mcal.inputNumber(userNumber)  
        print(userNumber3)

#resultUser + Third User's number (Second calculation)
        resultUser1 = mcal.inputSymbol1(operator, resultUser, userNumber3)  
        print(resultUser1)

#Exit from program
    except SystemExit:  
        exit()

#If userNumber == str or operator
    except:
        print("Input number!!!")
        continue


