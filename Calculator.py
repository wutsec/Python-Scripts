print('Basic Python-Based Calculator') #Intro
print('Developed By delorean')
print('~')
print('Select Operation')
print('1. +')
print('2. -')
print('3. *')
print('4. /')
print('~')

operation = input() #Defines the mathematical operation type

print('Enter First Number')
num1 = float(input()) #First number in equation
print('Enter Second Number')
num2 = float(input()) #Second number in equation

if operation == '1': #Addition
    print('Output')
    print(num1 + num2)
    
elif operation == '2': #Subtraction
    print('Output')
    print(num1 - num2)
    
elif operation == '3': #Multiplication
    print('Output')
    print(num1 * num2)

elif operation == '4': #Division
    print('Output')
    print(num1 / num2)

else:
  print('Invalid Operation - Please Restart Script') #Invalid operation error message
  input()
