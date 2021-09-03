# >>>Victor Andres Barilin<<<

from read_number import read_number


number = ''
while number != 'exit':
    number = input('Escriba un numero entero o "exit" para salir:\n>>>')

    try:
        int(number)
        print('===============================================================================')
        print('===============================================================================')
        print(read_number(number))
        print('===============================================================================')
        print('===============================================================================\n')

    except:
        if number == 'exit':
            print('-----\nAdios\n-----')

        else:
            print('El valor ingresado no es un entero.')