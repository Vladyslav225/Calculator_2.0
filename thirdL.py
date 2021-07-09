#for


# listNum = [1, 2, 3, 4, 5]

#countNum = 0    #Allways 0
#for num in listNum:
#    if num in [3, 4]:
#        countNum +=num
#        print(countNum)

#for strI in "hello":
#    if strI == "l":
#        continue

#    print(strI)
#    if strI == "l":
#        break




#while

#n = 0
#while n<=10:
#    print(n)
#    n += 1  # n = n + 1


#bool_while = True
#while bool_while:
#    value = input(": ")
#    if value == "exit":
#        break

#    if value.isalpha():
#        print("try!")
#        continue



#def


def functionInput():
    try:
        num = input("InputNumber: ")
        return float(num)
    except:
        return None

if __name__ == "__main__":
    while True:

        print("Start")

        num1 = functionInput()
        if not num1:
            continue

        num2 = functionInput()
        if not num2:
            continue
        print(num1 + num2)