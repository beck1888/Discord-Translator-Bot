# Translator Bot Help

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

*COMING SOON:* `/credits` - Shows a list of recourses used in making this project

`/help` - Shows this menu

`/report {your_message}` - Use this to report an issue you've found

`/request {a_feature_you_would_like}` - Use this to request a feature

`/version` - Shows the current bot version

The dev will see a log of your reports and requests. Your username will be recorded too.

The dev *may* reach out to you with further questions. You can respond if you want, but no pressure.

**Dev commands**

These following commands can be used, as they are helpful in the development and testing of the bot, but they will eventually be removed. Please don't misuse!

`/space` - Use this to create a bunch of new lines to add space into the chat history which makes it easier to see

`{shutdown_code}` - Shutdown from the Discord app. Will have to reactivate from VS Code. Pin is in VS Code terminal.

## My command isn't working!

1. Make everything lowercase

2. Review command format above

3. Check spelling and that you typed in English

4. Submit a report as specified above