# Need to import this library since all the mathematical operations supported by this  module are in it.
import math

# To prompt user the mathematical operation menu.
while True:
    print("\n\tWelcome to Mathematics Calculator!\n\nChoose the math operation.\n\n0 - Addition\n1 - Substraction\n2 - Multiplication\n3 - Division\n4 - Mudolu\n5 - Raising to the power\n6 - Square root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent")

    oper = input("\nYour option from the menu: ")

    # Addition
    if oper == '0':
        val1 = float(input("\n First value: "))
        val2 = float(input("\n Second value: "))
        print("\nResult of %f and %f is :%f" % (val1, val2, val1 + val2))

        # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
        back = input("\n Go back to the main menu? (y/n) ")

        if back == 'y':
            continue
        else:
            break
    
    # Substraction
    elif oper == "1":
        val1 = float(input("\n First value: "))
        val2 = float(input("\n Second value: "))
        print("\nResult of %f and %f is :%f" % (val1, val2, val1 - val2))

        # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
        back = input("\n Go back to the main menu? (y/n) ")

        if back == 'y':
            continue
        else:
            break
    
    # Multiplication
    elif oper == '2':
        val1 = float(input("\n First value: "))
        val2 = float(input("\n Second value: "))
        print("\nResult of %f and %f is :%f" % (val1, val2, val1 * val2))

        # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
        back = input("\n Go back to the main menu? (y/n) ")

        if back == 'y':
            continue
        else:
            break

    # Division
    elif oper == '3':
        val1 = float(input("\n First value: "))
        val2 = float(input("\n Second value: "))
        print("\nResult of %f and %f is :%f" % (val1, val2, val1 / val2))

        # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
        back = input("\n Go back to the main menu? (y/n) ")

        if back == 'y':
            continue
        else:
            break
    
    # Modulo
    elif oper == '4':
        val1 = float(input("\n First value: "))
        val2 = float(input("\n Second value: "))
        print("\nResult of %f and %f is :%f" % (val1, val2, val1 % val2))

        # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
        back = input("\n Go back to the main menu? (y/n) ")

        if back == 'y':
            continue
        else:
            break
    
    # Raising to the power
    elif oper == '5':
        val1 = float(input("\n First value for base: "))
        val2 = float(input("\n Second value for power: "))
        print("\nResult of %f and %f is :%f" % (val1, val2, val1 ** val2))

        # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
        back = input("\n Go back to the main menu? (y/n) ")

        if back == 'y':
            continue
        else:
            break
    
    # Square Root
    elif oper == '6':
        val1 = float(input("\n Value to square root: "))
        print("\nResult of %f is :%f" % (val1, math.sqrt(val1)))

        # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
        back = input("\n Go back to the main menu? (y/n) ")

        if back == 'y':
            continue
        else:
            break

    # Logarithm
    elif oper == '7':
        val1 = float(input("\n Enter the value to log of base 2: "))
        print("\nResult of %f is :%f" % (val1, math.log(val1,2)))

        # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
        back = input("\n Go back to the main menu? (y/n) ")

        if back == 'y':
            continue
        else:
            break

     # Sine
    elif oper == '8':
        val1 = float(input("\n Enter the value (in degrees) for calculating the sine: "))
        print("\nResult of %f is :%f" % (val1, math.sin(math.radians(val1))))

        # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
        back = input("\n Go back to the main menu? (y/n) ")

        if back == 'y':
            continue
        else:
            break

     # Cosine
    elif oper == '9':
        val1 = float(input("\n Enter the value (in degrees) for calculating the cosine: "))
        print("\nResult of %f is :%f" % (val1, math.cos(math.radians(val1))))

        # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
        back = input("\n Go back to the main menu? (y/n) ")

        if back == 'y':
            continue
        else:
            break
    
     # Tangent
    elif oper == '10':
        val1 = float(input("\n Enter the value (in degrees) for calculating the tangent: "))
        print("\nResult of %f is :%f" % (val1, math.tan(math.radians(val1))))

        # This will prompt user either to stay in the while loop. if not the loop will break and exit the operation menu.
        back = input("\n Go back to the main menu? (y/n) ")

        if back == 'y':
            continue
        else:
            break

    # Handling the invalid options

    else:
        print("\nInvalid option!\n")
        continue

# End of the program

