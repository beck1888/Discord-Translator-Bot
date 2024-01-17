## Bot functions.py

## Import block
import datetime
from data_structures import word_convert

## Helper functions: These assist the 'responds' function which processes and responds to the command

# Parse out the word into the command parts
def parse(command):
    # Build out words
    word = ''
    cmd_list = []
    for letter in command:
        if letter ==  ' ':
            cmd_list.append(word)
            word = ''
        else:
            word += letter
        
    cmd_list.append(word) # Adds the last word

    print(cmd_list)



## MAIN FUNCTION: Command processing
def respond(command, username): # Take in command and username

    # Determine mode
    if command[11] == 'w': # Translating a word
        return word_convert.get(command[11:])


    #parse(command)

    # After figuring out what to say, reply to the function which responds to the server to send a message
    # return reply