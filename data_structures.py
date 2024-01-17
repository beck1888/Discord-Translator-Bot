### English to Spanish dictionary
word_convert = {
    "time":"el tiempo",
    "person":"la persona",
    "year":"el año",
    "way":"la manera",
    "day":"el día",
    "thing":"la cosa",
    "man":"el hombre",
    "life":"la vida",
    "hand":"la mano",
    "part":"la parte",
    "hello":"hola"    
}

#### Structure for building the conjugation object
class conjugate:
    def __init__(self, verb, subject, tense):
        self.verb = verb
        self.subject = subject
        self.tense = tense

### Tense conjugations
ar_endings_present = {
    "i":"o",
    "you":"as",
    "he":"a",
    "she":"a",
    "it":"a",
    "we":"amos",
    "they":"an" # Only using they as a plural pronoun for now, specify also they for objects
}

er_endings_present = {
    "i":"o",
    "you":"es",
    "he":"e",
    "she":"e",
    "it":"e",
    "we":"emos",
    "they":"en" # Only using they as a plural pronoun for now, specify also they for objects
}