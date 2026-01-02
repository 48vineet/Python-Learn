
# * Introduction to Strings
# can be declare in 3 forms

name1 = "Vineet"
name2 = 'Vineet'
name3 = ''' Vineet '''


# * STRING SLICING
# ? The index in a sting starts from 0 to(length - 1) in Python. In order to slice a string, we use
# ? the following syntax:


# todo sl = name1[firstIndex: lastMinusOneIndex]
# * for example
# name1[0:3]  # todo "Vin" --> charecter from 0 to 3
# name1[1:3]  # todo "in" --> charecter from 1 to 3

name = "vineetmanoharmali"
print(name[1:12:3])  # ieah

# ? capitalize()	Converts the first character to upper case

# ? casefold()	Converts string into lower case

# ? center()	Returns a centered string

# ? count()	Returns the number of times a specified value occurs in a string

# ? encode()	Returns an encoded version of the string

# ? endswith()	Returns true if the string ends with the specified value

# ? expandtabs()	Sets the tab size of the string

# ? find()	Searches the string for a specified value and returns the position of where it was found

# ? format()	Formats specified values in a string

# ? format_map()	Formats specified values from a dictionary in a string

# ? index()	Searches the string for a specified value and returns the position of where it was found

# ? isalnum()	Returns True if all characters in the string are alphanumeric

# ? isalpha()	Returns True if all characters in the string are in the alphabet

# ? isascii()	Returns True if all characters in the string are ascii characters

# ? isdecimal()	Returns True if all characters in the string are decimals

# ? isdigit()	Returns True if all characters in the string are digits

# ? isidentifier()	Returns True if the string is an identifier

# ? islower()	Returns True if all characters in the string are lower case

# ? isnumeric()	Returns True if all characters in the string are numeric

# ? isprintable()	Returns True if all characters in the string are printable

# ? isspace()	Returns True if all characters in the string are whitespaces

# ? istitle()	Returns True if the string follows the rules of a title

# ? isupper()	Returns True if all characters in the string are upper case

# ? join()	Converts the elements of an iterable into a string

# ? ljust()	Returns a left justified version of the string

# ? lower()	Converts a string into lower case

# ? lstrip()	Returns a left trim version of the string

# ? maketrans()	Returns a translation table to be used in translations

# ? partition()	Returns a tuple where the string is parted into three parts

# ? replace()	Returns a string where a specified value is replaced with a specified value

# ? rfind()	Searches the string for a specified value and returns the last position of where it was found

# ? rindex()	Searches the string for a specified value and returns the last position of where it was found

# ? rjust()	Returns a right justified version of the string

# ? rpartition()	Returns a tuple where the string is parted into three parts

# ? rsplit()	Splits the string at the specified separator, and returns a list

# ? rstrip()	Returns a right trim version of the string

# ? split()	Splits the string at the specified separator, and returns a list

# ? splitlines()	Splits the string at line breaks and returns a list

# ? startswith()	Returns true if the string starts with the specified value

# ? strip()	Returns a trimmed version of the string

# ? swapcase()	Swaps cases, lower case becomes upper case and vice versa

# ? title()	Converts the first character of each word to upper case

# ? translate()	Returns a translated string

# ? upper()	Converts a string into upper case

# ? zfill()	Fills the string with a specified number of 0 values at the beginning

#! Note: All string methods returns new values. They do not change the original string.

# * Escape Sequnce Charecter
# \n	Newline – Moves the cursor to the next line.
# \t	Tab – Adds a horizontal tab.
# \\	Backslash – Inserts a literal backslash.
# \'	Single Quote – Inserts a single quote inside a single-quoted string.
# \"	Double Quote – Inserts a double quote inside a double-quoted string.

#! Practice Set
# 1. Write a python program to display a user entered name followed by Good
# Afternoon using input() function.
# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
# 3. Write a program to detect double space in a string.
# 4. Replace the double space from problem 3 with single spaces.
# 5. Write a program to format the following letter using escape sequence
# characters.
# letter = "Dear Harry, this python course is nice. Thanks!"

name = input("Enter Name :")
print(f"Good Evening Mr/Mrs {name}")
