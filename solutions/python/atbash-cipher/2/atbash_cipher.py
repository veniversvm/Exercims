PLAIN = "abcdefghijklmnopqrstuvwxyz123"
CIPHER = "zyxwvutsrqponmlkjihgfedcba123"

def encode(plain_text):
    encoded = [
        PLAIN[CIPHER.index(letter)] if i % 5 != 0 
        else " "+PLAIN[CIPHER.index(letter)] 
        for i, letter 
        in enumerate(plain_text.lower().replace(" ", "").replace(".", "").replace(",", ""))
    ]
    return "".join(encoded).strip()



def decode(ciphered_text):
    decoded = [CIPHER[PLAIN.index(letter)] for letter in ciphered_text.lower().replace(" ", "").replace(".", "")]
    return "".join(decoded)