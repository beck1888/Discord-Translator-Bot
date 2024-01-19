# Translator Bot Help

## Features and how to use them

**Translate words**
- Use this format: `/translate {word}`
    - Replace *{word}* with the word you want to translate
    - This only works from English -> Spanish
    - Only a VERY small list of words are supported right now


**Conjugate verbs**
- Use this format: `/conjugate {infinitive_verb} {english_subject} {english_tense}`
    - Replace the verb, subject, and tense with what you want
        - Remove the curly brackets!

EXAMPLE: to conjugate 'hablar' in the 'present' form where 'you' is the subject, type this: 

`/conjugate hablar you present`

Notes about the conjugator:

1. Irregular verbs will be rejected.

2. As of now, only the present and future tense are supported

3. Using *they* as a subject will always use the 3rd person, plural version of they for simplicity, despite the fact that it can be used as a singular pronoun

**Other commands**

`/version` - Shows the current bot version

`/help` - Shows this menu

*COMING SOON:* `/report {your_message}` - Use this to report an issue you've found

## My command isn't working!

1. Try making everything lowercase

2. Reference the guide above for command format

3. Check spelling

4. Submit a report as specified above