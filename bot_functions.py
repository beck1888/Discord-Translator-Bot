## Bot functions.py

## Give error is this file is ran instead of main.py
if __name__ == '__main__':
    import os
    import playsound
    # playsound.playsound('misc/error.mp3', False)
    os.system('''
              osascript -e 'tell app "Visual Studio Code" to display dialog "Oops! 'bot_functions.py' cannot be run!\n\nDid you mean to run main.py?" with icon stop buttons {"Dismiss"} default button "Dismiss"'
              ''')
    exit()


## Import block
import datetime
from data_structures import *


## Special functions: main aid to helper
def conjugate(verb, subject, tense):
    # Make sure verb in an infinitive
    verb_lower = verb.lower()
    if verb_lower[-2:] not in ['ar', 'er', 'ir']:
        return f"Oops! {verb} is not an infinitive verb!"

    # Check for irregular verbs first
    if tense == 'present':
        if verb in present_irregulars:
            return "Sorry, but I can't conjugate irregular verbs yet!"
    elif tense == 'future':
        if verb in future_irregulars:
            return "Sorry, but I can't conjugate irregular verbs yet!"
        
    # Check if known subject was passed
    if subject.lower() not in ["i", "you", "he", "she", "it", "we", "they"]:
        return f"I don't know the subject '{subject}'"
        
    # Enforce known tense is passed
    if tense.lower() not in ['present', 'future']:
        if tense.lower() in ['past', 'preterit', 'imperfect', 'command', 'conditional', 'subjunctive']:
            return f'The {tense} tense will be added soon!'
        else:
            return f"'{tense}' is not a real Spanish tense!"

    # Then if not irregular, proceed to conjugate
    if tense == 'present': # Conjugation for the present tense
        span_subject = convert_subject[subject]
        span_verb_root = verb[:-2] # Trim off the infinitive ending
        # Determine ending type
        if verb[-2:] == 'ar': # For AR endings
            conjugated_phrase = f'Here you go: {span_subject} {span_verb_root}{ar_endings_present[subject]}'
        elif verb[-2:] == 'er':
            conjugated_phrase = f'Here you go: {span_subject} {span_verb_root}{er_endings_present[subject]}'
        elif verb[-2:] == 'ir':
            conjugated_phrase = f'Here you go: {span_subject} {span_verb_root}{ir_endings_present[subject]}'
        else:
            return 'Wut?'
        # Return the relevant conjugation from above to the function call in the respond function
        return conjugated_phrase
    elif tense == 'future': # Future tense
        span_subject = convert_subject[subject]
        conjugated_phrase = f'Here you go: {span_subject} {verb}{future_endings[subject]}'
        return conjugated_phrase
    else:
        return 'I cant conjugate that tense yet!'


## Helper functions: These assist the 'responds' function which processes and responds to the command

def parse_for_conj(full_command): # Take inputs in ENGLISH
    # Count spaces
    spaces = 0
    for char in full_command:
        if char == ' ':
            spaces += 1
    # Make sure command with 3 args was given
    if spaces != 3:
        return 'Improper command format!'
    # Lowercase everything
    full_command = full_command.lower()
    # Turn into relevant parts after the slash command
    directions = full_command[11:]
    # Break into the parts of word, subject, and tense
    verb, subject, tense = directions.split()
    # Build the special object for the conjugation process
    # thing_to_conj(verb,subject,tense)
    conjugated_subject_and_verb = conjugate(verb, subject, tense)
    return f'{conjugated_subject_and_verb}'
    # return f'It sounds like you are trying to conjugate the verb {verb} in the {tense} tense with the subject of {subject}.\nI will get right on that once Beck programs me to lol!'




## MAIN FUNCTION: Command processing
def respond(command, username): # Take in command and username

    if command == '/space':
        return '.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.'

    # If the user wants to do a translation
    # Format: /translate {word}
    if command[0:10] == '/translate': # If the command is to translate
        word = command[11:] # Use only the word part and not the first part of the string
        word = word.lower()

        # See if the word is in the dictionary
        if word not in word_convert: # Send error if word is not mapped
            with open('unknown.txt', 'a') as unknown:
                unknown.write(f'{word}\n\n')
            return f"I'm sorry, {username}, but I don't know how to translate '{word}' into Spanish yet!\nHowever, it has been added to the project's logs and will be added soon!"
        # Can continue is the word is mapped
        translation = word_convert[word]
        return f"In Spanish, '{word}' is: {translation}"
    
    # If the user wants to do a conjugation
    # Format: /conjugate {infinitive} {subject} {tense}
    # Supported tenses
    if command[0:10] == '/conjugate':
        return parse_for_conj(command)


    

    # IF NO OUTPUT IS GENERATED, FORCE STOP THE REPLY
    return None