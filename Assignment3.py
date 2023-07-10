number1 = float(input('Enter the first number:'))
number2 = float(input('Enter the Second number:'))

choice = int(input('Enter your choice:'))

if choice == 1:
    print(number1 + number2) 
elif choice == 2:
    print(number1 - number2) 
elif choice == 3:
    print(number1 / number2) 
elif choice == 4:
    print(number1 * number2) 
elif choice == 5:
    print(number1 // number2)  
elif choice == 6:
    print(number1 % number2) 
elif choice == 7:
    print(number1 ** number2)
else:
    print('incorrect choice ')
    print("Please enter correct choice")