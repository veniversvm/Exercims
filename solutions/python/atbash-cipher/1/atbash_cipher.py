PLAIN = "abcdefghijklmnopqrstuvwxyz123"
CIPHER = "zyxwvutsrqponmlkjihgfedcba123"

def encode(plain_text):
    encoded = ""
    i = 0
    for letter in plain_text.lower().replace(" ", "").replace(".", "").replace(",", ""):
        i += 1
        index = PLAIN.index(letter)
        encoded += CIPHER[index]
        if i % 5 == 0:
            encoded += " "
    return encoded.strip()


def decode(ciphered_text):
    decoded = ""
    for letter in ciphered_text.lower().replace(" ", "").replace(".", ""):
        index = PLAIN.index(letter)
        decoded += CIPHER[index]

    return decoded
