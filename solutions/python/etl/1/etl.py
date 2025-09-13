def transform(legacy_data: dict):
    my_dict = {}
    for keys, letters in legacy_data.items():
        for letter in letters:
            d = dict.fromkeys(letter.lower(), keys)
            my_dict.update(d)
    return my_dict
