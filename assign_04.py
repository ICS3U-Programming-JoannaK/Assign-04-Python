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
            # CAST it to a an integer
            start_integer = int(start_string)
            try:
                # Asking user to input their ending angle and assign it to a string
                end_string = input("Enter the ending angle: ")
                # CAST it to an integer
                end_integer = int(end_string)
                # Check if the angles are in the needed range
                if start_integer >= 0 and end_integer <= 360:
                    # Exits the loop when the condition is met
                    break
                else:
                    print(
                        "Angles should be in the range of 0 and 360, and starting angle must be smaller than ending angle. "
                    )
            # Catches erroneous input for the ending angle
            except Exception:
                print(
                    "{} is not a valid input. Please enter an angle between 0 and 360".format(
                        end_string
                    )
                )
                # Catches erroneous input for the starting angle
        except Exception:
            print(
                "{} is not a valid input. Please enter an angle between 0 and 360".format(
                    start_string
                )
            )
    # This is the table header/title
    print("Angle\t\tTan")
    print("---------------------------\n")
    # This loop goes through the angle range given in steps of 10 degrees
    for angle in range(start_integer, end_integer + 1, 10):
        # Check for where the angle is undefined
        if angle % 180 == 90:
            # This prints the word "Undefined"
            print("\n")
            print("{}\t\tUndefined".format(angle))
        else:
            # Converts degrees to radians
            radians = math.radians(angle)
            # Calculates the tangent of the angle
            tangent_number = math.tan(radians)
            print("\n")
            # Prints the tangent of the angle in 5 decimal places
            print("{}\t\t{:,.5f}\n".format(angle, tangent_number))


if __name__ == "__main__":
    main()
