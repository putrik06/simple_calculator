# Need to import this library since all the mathematical operations supported by this  module are in it.
# import math

# # To prompt user the mathematical operation menu.
# while True:
#     print("\n\tWelcome to Mathematics Calculator!\n\nChoose the math operation.\n\n0 - Addition\n1 - Substraction\n2 - Multiplication\n3 - Division\n4 - Mudolu\n5 - Raising to the power\n6 - Square root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent")

#     oper = input("\nYour option from the menu: ")

#     # Addition
#     if oper == '0':
#         val1 = float(input("\n First value: "))
#         val2 = float(input("\n Second value: "))
#         print("\nResult of %f and %f is :%f" % (val1, val2, val1 + val2))

#         # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
#         back = input("\n Go back to the main menu? (y/n) ")

#         if back == 'y':
#             continue
#         else:
#             break
    
#     # Substraction
#     elif oper == "1":
#         val1 = float(input("\n First value: "))
#         val2 = float(input("\n Second value: "))
#         print("\nResult of %f and %f is :%f" % (val1, val2, val1 - val2))

#         # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
#         back = input("\n Go back to the main menu? (y/n) ")

#         if back == 'y':
#             continue
#         else:
#             break
    
#     # Multiplication
#     elif oper == '2':
#         val1 = float(input("\n First value: "))
#         val2 = float(input("\n Second value: "))
#         print("\nResult of %f and %f is :%f" % (val1, val2, val1 * val2))

#         # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
#         back = input("\n Go back to the main menu? (y/n) ")

#         if back == 'y':
#             continue
#         else:
#             break

#     # Division
#     elif oper == '3':
#         val1 = float(input("\n First value: "))
#         val2 = float(input("\n Second value: "))
#         print("\nResult of %f and %f is :%f" % (val1, val2, val1 / val2))

#         # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
#         back = input("\n Go back to the main menu? (y/n) ")

#         if back == 'y':
#             continue
#         else:
#             break
    
#     # Modulo
#     elif oper == '4':
#         val1 = float(input("\n First value: "))
#         val2 = float(input("\n Second value: "))
#         print("\nResult of %f and %f is :%f" % (val1, val2, val1 % val2))

#         # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
#         back = input("\n Go back to the main menu? (y/n) ")

#         if back == 'y':
#             continue
#         else:
#             break
    
#     # Raising to the power
#     elif oper == '5':
#         val1 = float(input("\n First value for base: "))
#         val2 = float(input("\n Second value for power: "))
#         print("\nResult of %f and %f is :%f" % (val1, val2, val1 ** val2))

#         # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
#         back = input("\n Go back to the main menu? (y/n) ")

#         if back == 'y':
#             continue
#         else:
#             break
    
#     # Square Root
#     elif oper == '6':
#         val1 = float(input("\n Value to square root: "))
#         print("\nResult of %f is :%f" % (val1, math.sqrt(val1)))

#         # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
#         back = input("\n Go back to the main menu? (y/n) ")

#         if back == 'y':
#             continue
#         else:
#             break

#     # Logarithm
#     elif oper == '7':
#         val1 = float(input("\n Enter the value to log of base 2: "))
#         print("\nResult of %f is :%f" % (val1, math.log(val1,2)))

#         # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
#         back = input("\n Go back to the main menu? (y/n) ")

#         if back == 'y':
#             continue
#         else:
#             break

#      # Sine
#     elif oper == '8':
#         val1 = float(input("\n Enter the value (in degrees) for calculating the sine: "))
#         print("\nResult of %f is :%f" % (val1, math.sin(math.radians(val1))))

#         # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
#         back = input("\n Go back to the main menu? (y/n) ")

#         if back == 'y':
#             continue
#         else:
#             break

#      # Cosine
#     elif oper == '9':
#         val1 = float(input("\n Enter the value (in degrees) for calculating the cosine: "))
#         print("\nResult of %f is :%f" % (val1, math.cos(math.radians(val1))))

#         # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
#         back = input("\n Go back to the main menu? (y/n) ")

#         if back == 'y':
#             continue
#         else:
#             break
    
#      # Tangent
#     elif oper == '10':
#         val1 = float(input("\n Enter the value (in degrees) for calculating the tangent: "))
#         print("\nResult of %f is :%f" % (val1, math.tan(math.radians(val1))))

#         # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
#         back = input("\n Go back to the main menu? (y/n) ")

#         if back == 'y':
#             continue
#         else:
#             break

#     # Handling the invalid options

#     else:
#         print("\nInvalid option!\n")
#         continue

# End of the program

# We can refactor the code by introducing the functions to handle the mathematical operation.
# There is redundancy  in the code and we need to remove it.

import math

def add(val1,val2):
    return val1 + val2

def subtract(val1,val2):
    return val1 - val2

def multiply(val1,val2):
    return val1 * val2

def divide(val1,val2):
    if val2 == 0:
        return  "Error! Division by zero is not allowed."
    return val1/val2

def modulus(val1,val2):
    return  val1 % val2

def power(val1,val2):
    return val1 ** val2

def square_root(val1):
    return math.sqrt(val1)

def logarithm(val1):
    return math.log(val1,2)

def sine(val):
    return math.sin(math.radians(val))

def cosine(val):
    return math.cos(math.radians(val))

def tangent(val):
    return math.tan(math.radians(val))

# Dictionary mapping operation codes to coressponding functions.

operations = {
    '0':add,
    '1':subtract,
    '2':multiply,
    '3':divide,
    '4':modulus,
    '5':power,
    '6':square_root,
    '7':logarithm,
    '8':sine,
    '9':cosine,
    '10':tangent
    }

print("\n\tWelcome to Mathematics Calculator!\n\nChoose the math operation.")

while True:
    print("\n".join([f"{key} - {value.__name__}" for key, value in operations.items()]))

    oper = input("\nYour option from the menu: ")

    if oper not in operations:
        print("\nInvalid option!\n")
        continue

    if oper in ['6', '7', '8', '9', '10']:
        val1 = float(input("\nEnter the value: "))
        result = operations[oper](val1)
    else:
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))
        result = operations[oper](val1, val2)

    print(f"\nResult: {result}")

    back = input("\nGo back to the main menu? (y/n) ")
    if back.lower() != 'y':
        break


