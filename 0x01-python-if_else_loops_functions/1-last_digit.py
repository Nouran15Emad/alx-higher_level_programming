#!/usr/bin/python3

# get random number
import random
number = random.randint(-10000, 10000)


# get the last digit
if number < 0:
    Last_digit = number % -10  # Get negative last digit for negative numbers
else:
    Last_digit = number % 10   # Get last digit for positive numbers

# Print the result based on the value of Last_digit
if Last_digit > 5:
    print("Last digit of {} is {} and is greater than 5"
          .format(number, Last_digit))
elif Last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, Last_digit))
else:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, Last_digit))
