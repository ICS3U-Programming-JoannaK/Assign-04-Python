#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: April 29, 2025
# This program catches erroneous input,
# and writes a program that generates the
# tan table for each degree (0 to 360).

import math

# Display greeting card
def main():
    print("*****************************************")
    print("*****************************************")
    print("***           Hello user !             **")
    print("*****************************************")
    print("*****************************************")
    print("\n")

# using a while true loop to repeatedly ask for valid angles from the user
    while True:
        # Asking the user to input their starting angle and assign it to a string
        start_string = input("Enter the starting angle: ")
        try:
            #CAST it to a an integer
            start_integer = int(start_string)
            try: 
                end_string = input("Enter the ending angle: ")
                end_integer = int(end_string)
                if start_integer >= 0 and end_integer <= 360:
                    break
                else:
                    print(
                    "Angles should be in the range of 0 and 360, and starting angle must be smaller than ending angle. "
                )
            except Exception:
                print(
                "{} is not a valid input. Please enter an angle between 0 and 360".format(
                    end_string
                )
            )
        except Exception:
            print(
                "{} is not a valid input. Please enter an angle between 0 and 360".format(
                    start_string
                )
            )
    print("Angle\t\tTan")
    print("---------------------------\n")
    for angle in range(start_integer, end_integer + 1, 10):
        if angle % 180 == 90:
            print("\n")
            print("{}\t\tUnderfined".format(angle))
        else:
            radians = math.radians(angle)
            tangent_number = math.tan(radians)
            print("\n")
            print("{}\t\t{:,.5f}\n".format(angle, tangent_number))


if __name__ == "__main__":
    main()
