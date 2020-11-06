# snake_case all in lowercase

# imports

#global vars

# functions


def clear():
    print('\n'*20)
    # HW: Python clear console
    # HW: Calculation AGE


def print_menu():
    print('***********************************')
    print('Welcome - PyCalc')
    print('***********************************')

    print('[1] Add')
    print('[2] Substract')
    print('[3] Multiplication')
    print('[4] Divide')
    print('[5] Caculate my age')
    print('[x] Exit')
    print('-'*20)  # repeat the char


# instructions

opc = ''

while(opc != 'x'):
    print_menu()
    opc = input('Please select an option:')

    if(opc != 'x'):
        print("You want to add 2 numbers")
        n1 = float(input("Give me first number:"))
        n2 = float(input("Give me second number:"))
        if(opc == '4' and n2 == 0):
            while(n2 == 0):
                print('Erro, Zero division not allowed')
                n2 = float(input("Give me second number:"))


#    elif(opc=='6')

    if(opc == '1'):
        result = n1+n2
    elif(opc == '2'):
        result = n1-n2
    elif(opc == '3'):
        result = n1*n2
    elif(opc == '4'):
        result = n1/n2

#    elif(opc == '6')

    print('Your result is:'+str(result))
    input('Enter to continue....')
    clear()


print("Good byte!!!")
