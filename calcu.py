#Python Basic Calcu // Feb.25,2021

def simple_calculator():

  print('Welcome! This is a basic calculator that can help you!\n')



  num1 = float(input('Enter the first number: '))
  op = input('Enter an Operator: ')
  num2 = float(input('Enter the second number: '))


  if op == '+':
    answer = str(num1 + num2)
    print('\nThe first number is ' + str(num1) + ' and will be added to ' + str(num2) + '. \n')
    print('The answer is: ' + answer)

  elif op == '-':
    answer = str(num1 - num2)
    print('\nThe first number is ' + str(num1) + ' and will be deducted to ' + str(num2) + '. \n')
    print('The answer is: ' + answer)

  elif op == 'x':

    answer = str(num1 * num2)
    print('\nThe first number is ' + str(num1) + ' and will be multiply to ' + str(num2) + '. \n')
    print('The answer is: ' + answer)

  elif op == '/':

   answer = str(num1 / num2)
   print('\nThe first number is ' + str(num1) + ' and will be divided to ' + str(num2) + '. \n')
   print('The answer is: ' + answer)

  else:
    print('invalid')


simple_calculator()
