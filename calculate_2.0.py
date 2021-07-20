import moduleCalculator as mcal     #Connecting the module



resultUser = " "
resultsUser = [ ]
userNumber = " "
operator = " "
firstNumber = " "
secondNumber = " "


print("To finish calculation write 'Clear' or 'Clean' ")
print("To finish calculation write 'Exit' ")

while True:

        while True:


#Firrst User's number        
                firstNumber = mcal.inputNumber(userNumber)  
                print(firstNumber)

                # userNumbers.append(userNumber)
                
                operator = mcal.inputSymbol(operator)  
                print(operator)

# #Second User's number        
#         secondNumber = mcal.inputNumber(userNumber)  
#         print(secondNumber)

# #Result
#         resultUser = mcal.resultUser(operator, firstNumber, secondNumber)
#         print(resultUser)

#         resultsUser.append(resultUser)

# #First User's number + Second User's number (First calculation)
#         operator = mcal.inputSymbol(operator)  
#         print(operator)

#         resultsUser = mcal.resultUser(operator, firstNumber, secondNumber)
#         print(resultsUser)

     
# #Third User's number
#         userNumber3 = mcal.inputNumber(userNumber)  
#         print(userNumber3)

# #resultUser + Third User's number (Second calculation)
#         resultUser1 = mcal.inputSymbol1(operator, resultUser, userNumber3)  
#         print(resultUser1)

# #Exit from program
#     except SystemExit:  
#         exit()

# #If userNumber == str or operator
#     except:
#         print("Input number!!!")
#         continue


