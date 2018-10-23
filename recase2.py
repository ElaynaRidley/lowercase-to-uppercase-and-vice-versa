'''
Program: recase2.py
Author: Elayna Ridley
Course: CSC 111L, Lab 4
Purpose: To print out the uppercase version given an input of a string and an input of "U",
or to print out the lowercase version given an input of a string and an input of "L".

Input: A string or characters, then a "U" or "L".
Output: An uppercase version of an input string given input "U",
or a lowercase version of an input string given input "L".
Algorithm: After inputting direction, determine if the direction is not a "U" or and "L".
If it isn't, exit the program.
If it is and "L", go through each character in the inputted string and detering if its ord is between the numbers 65 and 90.
If it is, add 32 to its ord. If it's not, leave it the same.
If the direction is "U", go through each character in the inputted string and see if its ord is between the numbers 97 and 122.
If it is, subtract 32 from its ord. If it isn't, leave it the same.
'''

import sys

input_string = input("Enter a string:")
direction = input("Enter U to uppercase, L to lowercase: ")

if direction != "U" and direction != "L":
	print('Your input should have been U or L')
	sys.exit()

newstring = ""
for ch in input_string:
	nch = ord(ch)
	if direction == "L" and nch >= 65 and nch <= 90:
		ch = chr(nch + 32)
	elif direction == "U" and nch >= 97 and nch <= 122:
		ch = chr(nch - 32)
	newstring += ch
	
print(newstring)
