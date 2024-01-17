## Bot functions.py

## Import block
import datetime
from data_structures import word_convert

## Helper functions: These assist the 'responds' function which processes and responds to the command

# Parse out the word into the command parts
# def parse(command):
#     pass
#     # Build out words
#     word = ''
#     cmd_list = []
#     for letter in command:
#         if letter ==  ' ':
#             cmd_list.append(word)
#             word = ''
#         else:
#             word += letter
        
#     cmd_list.append(word) # Adds the last word

#     print(cmd_list)



## MAIN FUNCTION: Command processing
def respond(command, username): # Take in command and username

    # Figure out what type of response to give
    if command[0:10] == '/translate': # If the command is to translate
        word = command[11:] # Use only the word part and not the first part of the string


    response = "//response here"

    return response