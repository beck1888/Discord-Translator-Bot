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
class thing_to_conj:
    def __init__(self, verb, subject, tense):
        self.verb = verb
        self.subject = subject
        self.tense = tense

## Convert English subject to Spanish
convert_subject = {
    "i":"yo",
    "you":"tú",
    "he":"él",
    "she":"ella",
    "it":"él",
    "we":"nosotros",
    "they":"ellos" # Only using they as a plural pronoun for now, specify also they for objects
}



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