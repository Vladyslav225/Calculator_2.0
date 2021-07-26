import module_Calculator__ as mc

userNumber = " "
operator = " "


user_Results = 0

print("""
     To exit the calculator, input 'Exit'
     To clear the calculator, input 'Clear'
""")

while True:

     firstNumber = mc.inputNumber(userNumber)
     print(firstNumber)

     while True:

          operator = mc.inputOperator(operator)
          print(operator)

          if not firstNumber:
               firstNumber = user_Results

          secondNumber = mc.inputNumber(userNumber)
          print(secondNumber)


          userResult = mc.calculation(firstNumber, secondNumber, operator)
          print(f"{firstNumber} {operator} {secondNumber} = {userResult}")
          user_Results = userResult

          firstNumber = None

