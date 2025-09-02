def is_isogram(string):
    strong_lower = string.lower().replace("-", "").replace(" ", "")
    return len((set(strong_lower))) == len(strong_lower)


