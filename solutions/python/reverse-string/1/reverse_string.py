def reverse(text):
    reverse_text = ""
    for i in range(len(text) -1, -1, -1):
        reverse_text += text[i]
    return reverse_text
