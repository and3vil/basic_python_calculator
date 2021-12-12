
print('Select operation to perform:')
print('1. Add')
print('2. Substract')
print('3. Multiply')
print('4. Divide')

operation = input()

if operation == '1':
    num1 = input("Enter a number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) + int(num2)))
elif operation == '2':
    num1 = input("Enter a number: ")
    num2 = input("Enter second number: ")
    print("The substraction is " + str(int(num1) - int(num2)))
elif operation == '3':
    num1 = input("Enter a number: ")
    num2 = input("Enter second number: ")
    print("The multiplication is " + str(int(num1) * int(num2)))
elif operation == '4':
    num1 = input("Enter a number: ")
    num2 = input("Enter second number: ")
    print("The division is " + str(int(num1) / int(num2)))
else:
    print("Invalid entry")



