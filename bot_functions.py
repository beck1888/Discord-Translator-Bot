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

    response = "//response here"

    return response