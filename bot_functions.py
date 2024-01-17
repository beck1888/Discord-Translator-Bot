## Bot functions.py

## Import block
import datetime
from data_structures import *


## Special functions: main aid to helpers

def conjugate(info_class):
    pass



## Helper functions: These assist the 'responds' function which processes and responds to the command

def parse_for_conj(full_command): # Take inputs in ENGLSIH
    # Turn into relevant parts after the slash command
    directions = full_command[11:]
    # Break into the parts of word, subject, and tense
    verb, subject, tense = directions.split()
    # Build the special object for the conjugation process
    thing_to_conj(verb,subject,tense)
    conjugate(thing_to_conj)
    return f'It sounds like you are trying to conjugate the verb {verb} in the {tense} tense with the subject of {subject}.\nI will get right on that once Beck programs me to lol!'




## MAIN FUNCTION: Command processing
def respond(command, username): # Take in command and username

    # If the user wants to do a translation
    # Format: /translate {word}
    if command[0:10] == '/translate': # If the command is to translate
        word = command[11:] # Use only the word part and not the first part of the string
        word = word.lower()

        # See if the word is in the dictionary
        if word not in word_convert: # Send error if word is not mapped
            return f"I'm sorry, {username}, but I don't know how to translate '{word}' into Spanish yet!\nHowever, I've logged this occurrence to be fixed!"
        # Can continue is the word is mapped
        translation = word_convert[word]
        return f"Great question, {username}! In Spanish, '{word}' is '{translation}'."
    
    # If the user wants to do a conjugation
    # Format: /conjugate {infinitive} {subject} {tense}
    # Supported tenses
    if command[0:10] == '/conjugate':
        return parse_for_conj(command)


    

    # IF NO OUTPUT IS GENERATED, FORCE STOP THE REPLY
    return False