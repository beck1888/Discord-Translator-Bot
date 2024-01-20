## TO-DOs

- Need to make function to check if valid command given

- When an unknown word is asked for, log it to a file so I can add it

- Add help guide with word fuzzing when an unknown command is given ⭐️

- Give error feedback via discord and reject command to prevent breaking script (try statements?)

- Add debug messages for each step in the terminal or a log (including message received but not replied to and message send)

- Deal with getting the gender of objects? IDK!!!
    - For now just default to the masculine pronouns

- Add reminder to use conjugations carefully


## Command format (don't include the dashes or brackets in the command)

wake word + mode + args

### Single word

`/translate --word --{english_word}`

---

### Conjugate a verb

`/translate --conj --{english_verb_infinitive} --subject --tense`

Reminders:

please deal with all words and commands only in lowercase for simplicity