def count_letter(word: str):
    letter_count = {}
    word_lower = word.lower()
    set_word = set(word_lower )

    for letter in set_word:
        letter_count[letter] = word_lower.count(letter)

    return letter_count


def find_anagrams(word, candidates):
    word_dict = count_letter(word)

    valid_candidates = [ c for c in candidates if word.lower() != c.lower() and word_dict == count_letter(c)]
    return valid_candidates


    
