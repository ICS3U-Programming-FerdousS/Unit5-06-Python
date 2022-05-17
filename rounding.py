#!/usr/bin/env python3
# Created By: Ferdous Sediqi
# Date: May, 16, 2022
# This program asks the user for a number with decimal 
# then calcuate and round number to the nearest
# decimal places of user choice. 


# function to round the number to nearest decimal number
def Rounding_Number(decimal_num, decimal_places):

    # doing calculation
    decimal_num = decimal_num * (10**decimal_places)
    decimal_num = decimal_num + 0.5
    decimal_num = int(decimal_num)
    decimal_num = decimal_num / (10**decimal_places)
    
    # display answer
    print("The number after rounding to decimal places is", decimal_num)


def main():

    # Get user inputs and convert it and int
    try:
        user_num_string = input("Enter your number with decimal: ")
        user_decimal_place_string = input("Enter your decimal places: ")
        user_num_float = float(user_num_string)
        user_decimal_place_int = int(user_decimal_place_string)
        print("")
        
        # check user input is 0 or less
        if (user_decimal_place_int <= 0 ):
            print("Decimal places cannot be less than 0.")
        else:
            # calling the function
            Rounding_Number(user_num_float, user_decimal_place_int)

    # invalid input
    except Exception:
        print("")
        print("Invalid input. Input was not a number.")


if __name__ == "__main__":
    main()
