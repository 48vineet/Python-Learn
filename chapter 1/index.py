# ============================ Python Full Course  ===========================================

# ? REPL reffers to Read Evaluates Print Loop it is used in terminal

#! CHAPTER 1 – PRACTICE SET


# * Write a program to print Twinkle twinkle little star poem in python.


# print("""Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.
# Twinkle, twinkle, little star,""")

# * Install an external module and use it to perform an operation of your interest.

# todo import cowsay
# my_fish = r'''
# \
#  \
#         /`·.¸
#      /¸...¸`:·
#  ¸.·´  ¸   `·.¸.·´)
# : © ):´;      ¸  {
#  `·.¸ `·  ¸.·´\`·¸)
#      `\\´´\¸.

# '''
# cowsay.cow("DSA samajh aa gaya bhai!")
# cowsay.draw('Sharks are my best friend', my_fish)

# * Write a python program to print the contents of a directory using the os module.
# * Search online for the function which does that.

import os
import shutil

import pyttsx3

# todo Creating Files
# Use open() with write mode to create a file
# with open('example.txt', 'w') as f:
#     f.write('Hello, World!')

# todo Renaming Files
# The os.rename() function renames a file:
# os.rename('example.txt', 'vineet.txt')

# todo Deleting Files
# Use os.remove() to delete a file
# os.remove("example.txt")

# todo Creating Directories
# Use os.mkdir() to create a single directory:
# os.mkdir('new_folder')

# todo For nested directories, use os.makedirs():
# os.makedirs('new_folder/child/grandchild')


# todo Listing Directory Contents
# os.listdir() returns a list of files and directories:
# contents = os.listdir('.')
# print(contents)

# todo Removing Directories
# Use os.rmdir() to remove an empty directory:
# os.rmdir('new_folder')

# todo For non-empty directories, use shutil.rmtree() from the shutil module.
# shutil.rmtree("new_folder")


# todo Getting Current Directory
# os.getcwd() returns the current working directory:
# current_dir = os.getcwd()
# print(current_dir)

# todo Joining Paths
# os.path.join() safely joins path components:
# full_path = os.path.join('folder', 'subfolder', 'file.txt')

# todo Checking Path Existence
# os.path.exists() checks if a path exists:
# if os.path.exists('file.txt'):
#     print("File exists")


# * testing and text to speak module
# Initialize the TTS engine
engine = pyttsx3.init()

# Text to be spoken
engine.say("Hello! Welcome to the vineet python directry.")

# Process and output the speech
engine.runAndWait()
