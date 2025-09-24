import re
OPENING_PATTERNS = ("(", "{", "[")
CLOSING_PATTERNS = (")", "}", "]")

def eval_is_paired(cleaned_string: str) -> bool:
    if cleaned_string == "" or input == None:
        return True
    if cleaned_string[0] not in OPENING_PATTERNS:
        return False
    
    opening_letter = cleaned_string[0]
    open_index = OPENING_PATTERNS.index(opening_letter)
    close_letter = CLOSING_PATTERNS[open_index]

    if cleaned_string[1] == close_letter:
        return eval_is_paired(cleaned_string[2:])
    if cleaned_string[-1] == close_letter:
        return eval_is_paired(cleaned_string[1:-1])
    return False


def is_paired(input_string: str) -> bool:
    cleaned_string = re.sub(r'[^,{}\[\],()]', '', input_string.replace(" ", ""))
    if len(cleaned_string) % 2 != 0:
        return False
    return eval_is_paired(cleaned_string)