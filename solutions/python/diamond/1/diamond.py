import string
ALPHABET = string.ascii_uppercase



def rows(letter):
    index = ALPHABET.index(letter.upper()) # * 2 + 1 if ALPHABET.index(letter.upper()) > 1 else 1
    if index == 0:
        return ["A"]

    diamon = []

    for i in range(index+1):
        line = [" "] * (index * 2 + 1) # creates a list filled with withe spaces
        if i == 0:
            line[index] = "A" 
            diamon.append("".join(line))
            continue
        position_letter = ALPHABET[i]
        line[index - i] = position_letter
        line[index + i] = position_letter
        diamon.append("".join(line))

    for i in range(index-1, -1, -1):
        line = [" "] * (index * 2 + 1) # creates a list filled with withe spaces
        if i == 0:
            line[index] = "A" 
            diamon.append("".join(line))
            continue
        position_letter = ALPHABET[i]
        line[index - i] = position_letter
        line[index + i] = position_letter
        diamon.append("".join(line))


    return diamon