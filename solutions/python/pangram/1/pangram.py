import re

def is_pangram(sentence):
    return len(set(list((re.sub(r'[^a-zA-Z]', '', sentence.lower())).replace(" ", "")))) == 26

