from string import ascii_lowercase, ascii_uppercase

lower_alphabet = tuple(ascii_lowercase)
upper_alphabet = tuple(ascii_uppercase)

def cipher_latter(letter, key, alphabet) -> str:
    letter_index =  alphabet.index(letter)
    return alphabet[letter_index + key - 26] if letter_index + key > 25 else alphabet[letter_index + key]

def rotate(text, key):
    while key > 25:
        key -= 26

    cipher = ""
    for  letter in text:
 
        if letter in lower_alphabet:
            cipher += cipher_latter(letter=letter, key=key, alphabet=lower_alphabet)
        elif letter in upper_alphabet:
            cipher += cipher_latter(letter=letter, key=key, alphabet=upper_alphabet)
            continue
        else:
            cipher += letter
        
    return cipher
