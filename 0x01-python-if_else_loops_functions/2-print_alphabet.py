#!/usr/bin/python3

alphabet = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))
print("{}".format(alphabet), end="")



# ord is a function that convert the character to its Ascii code
# ex: ord('a') = > 97
# and that is because for in range work on numbers
# so we need to convert letters to numbers then reconvert them to letters
# using chr function  chr(97)  = >
#  'a' when print
