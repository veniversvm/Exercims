def translate(text: str) -> str:
    words = text.split()
    translated_words = []

    for word in words:
        if word.startswith(('a', 'e', 'i', 'o', 'u', 'xr', 'yt')):
            translated_words.append(word + "ay")
            continue

        consonant_cluster = ""
        rest_of_word = word
        for i, letter in enumerate(word):
            if letter == 'q' and i + 1 < len(word) and word[i+1] == 'u':
                consonant_cluster += "qu"
                rest_of_word = word[i+2:]
                break
            if letter == 'y' and i > 0:
                rest_of_word = word[i:]
                break
            if letter in 'aeiou':
                rest_of_word = word[i:]
                break
            consonant_cluster += letter
        
        if rest_of_word == word: 
             if 'y' in word:
                 y_index = word.find('y')
                 consonant_cluster = word[:y_index]
                 rest_of_word = word[y_index:]

        translated_words.append(rest_of_word + consonant_cluster + "ay")

    return " ".join(translated_words)