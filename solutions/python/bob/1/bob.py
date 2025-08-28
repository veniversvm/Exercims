import re
def response(hey_bob):
    hey_bob = hey_bob.strip()
    question = len(hey_bob) > 0 and "?" == hey_bob[-1]
    cleaned_string = re.sub(r'[^A-Za-z\s?]', '', hey_bob)
    if cleaned_string == "": 
        return "Fine. Be that way!"
    if question and cleaned_string.isupper() and cleaned_string  == cleaned_string.upper():
        return "Calm down, I know what I'm doing!"
    if question:
        return "Sure."
    if cleaned_string.isupper() and cleaned_string  == cleaned_string.upper() and len(hey_bob) > 0:
        return "Whoa, chill out!" 
    else:
        return "Whatever." 

   
    print(cleaned_string) # Output: "Text with numbers  and symbols "