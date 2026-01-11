# CHAPTER 9 – FILE I/O
# ? The random-access memory is volatile, and all its contents are lost once a program
# ? terminates. In order to persist the data forever, we use files.
# ? A file is data stored in a storage device. A python program can talk to the file by reading
# ? content from it and writing content to it.

# * TYPE OF FILES.
# There are 2 types of files:
# ? 1. Text files(.txt, .c, etc)
# ? 2. Binary files(.jpg, .dat, etc)

# * OPENING A FILE
# *Python has an open() function for opening files. It takes 2 parameters:  filename and
# *mode.
# # open("filename", "mode of opening(read mode by default)")
# ?open("this.txt", "r")

# * READING A FILE IN PYTHON
# # Open the file in read mode
# ? f = open("this.txt", "r")
# # Read its contents
# ? text = f.read()
# # Print its contents
# ? print(text)

# Close the file
# f.close()

# f.readline()  # Read one line from the file.


# * MODES OF OPENING A FILE
# ? r – open for reading
# ? w - open for writing
# ? a - open for appending
# ? + - open for updating.
# ? ‘rb’ will open for read in binary mode.
# ? ‘rt’ will open for read in text mode.

# WRITE FILES IN PYTHON
# # Open the file in write mode
# ? f = open("this.txt", "w")
# # Write a string to the file
# ? f.write("this is nice")
# # Close the file
# ? f.close()

# WITH STATEMENT
# file
# ? with open("this.txt", "r") as f:
# ?     # Read the contents of the file
# ? text = f.read()
# # Print the contents
# ? print(text)

# * CHAPTER 9 – PRACTICE SET
# 1. Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

# 2. The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hi
# score whenever the game() function breaks the Hi-score.

# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.

# 4. A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with  # by updating the same file.

# 5. Repeat program 4 for a list of such words to be censored.

# 6. Write a program to mine a log file and find out whether it contains ‘python’.

# 7. Write a program to find out the line number where python is present from ques 6.

# 8. Write a program to make a copy of a text file “this. txt”

# 9. Write a program to find out whether a file is identical & matches the content of
# another file.

# 10. Write a program to wipe out the content of a file using python.

# 11. Write a python program to rename a file to "renamed_by_ python.txt.

# with open("chapter 9/text.txt", "r") as f:
#     r = f.read()

# if "twinkle" in r:
#     print("it contains")


# Solution for Problem 2: High Score Manager
import random


def game():
    """Simulates a game and returns a score"""
    print("Playing game...")
    score = random.randint(1, 100)
    print(f"Your score: {score}")
    return score


# Read the current high score
try:
    with open("chapter 9/Hi-score.txt", "r") as f:
        content = f.read()
        hiscore = int(content) if content.strip() else 0
except FileNotFoundError:
    hiscore = 0

print(f"Current Hi-score: {hiscore}")

# Play the game
score = game()

# Update high score if broken
if score > hiscore:
    with open("chapter 9/Hi-score.txt", "w") as f:
        f.write(str(score))
    print(f"🎉 New Hi-score! {score}")
else:
    print(
        f"Try again! You need {hiscore - score} more points to beat the high score.")
