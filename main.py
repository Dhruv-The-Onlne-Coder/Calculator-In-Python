import numpy

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculator():
    print("1. ADD")
    print("2. SUB")
    print("3. MUL")
    print("4. DIV")
    print("5. SQR")
    print("6. CUBE")
    print("7. SQRT")
    print("8. CBRT")
    
    while True:
        try:
            ope = int(input("Enter The Required Operation: "))
        except ValueError:
            print("Enter a number from 1 to 8.")
            continue
        
        if ope == 1:
            num1 = get_float_input("Enter num 1: ")
            num2 = get_float_input("Enter num 2: ")
            result = num1 + num2
            print(result)
        elif ope == 2:
            num1 = get_float_input("Enter num 1: ")
            num2 = get_float_input("Enter num 2: ")
            result = num1 - num2
            print(result)
        elif ope == 3:
            num1 = get_float_input("Enter num 1: ")
            num2 = get_float_input("Enter num 2: ")
            result = num1 * num2
            print(result)
        elif ope == 4:
            num1 = get_float_input("Enter num 1: ")
            num2 = get_float_input("Enter num 2: ")
            result = num1 / num2
            print(result)
        elif ope == 5:
            num1 = get_float_input("Enter num: ")
            result = num1 * num1
            print(result)
        elif ope == 6:
            num1 = get_float_input("Enter num: ")
            result = num1 * num1 * num1
            print(result)
        elif ope == 7:
            num1 = get_float_input("Enter num: ")
            result = numpy.sqrt(num1)
            print(result)
        elif ope == 8:
            num1 = get_float_input("Enter num: ")
            result = numpy.cbrt(num1)
            print(result)
        else:
            print("Enter a number from 1 to 8.")

        l_inp = input("Do you want to calculate again? (y/n): ").lower()
        if l_inp != "y":
            break

calculator()
