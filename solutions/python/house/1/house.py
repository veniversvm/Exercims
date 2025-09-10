END_VERSES = [
    "the house that Jack built.",
    "the malt",
    "the rat",
    "the cat",
    "the dog",
    "the cow with the crumpled horn",
    "the maiden all forlorn",
    "the man all tattered and torn",
    "the priest all shaven and shorn",
    "the rooster that crowed in the morn",
    "the farmer sowing his corn",
    "the horse and the hound and the horn",
]

START_VERSES = [
    "This is",
    "that belonged to",
    "that kept",
    "that woke",
    "that married",
    "that kissed",
    "that milked",
    "that tossed",
    "that worried", # (8) 9
    "that killed", # (9) 10
    "that ate", # (10) 11
    "that lay in", # (11) 12
]


def get_recite(start_verse, end_verse):
    verses = START_VERSES[0] + " " + END_VERSES[end_verse-1]
    len_v = len(START_VERSES)
    verses_position_start = len_v - start_verse + 1
    verses_position_end = end_verse - 2

    while  verses_position_start < len_v:
        start = START_VERSES[verses_position_start]
        end =  END_VERSES[verses_position_end ]
        verses += " " + start + " " + end
        verses_position_start += 1
        verses_position_end -= 1

    return verses

def recite(start_verse, end_verse):
    verses = []

    while start_verse <= end_verse:
        verses.append(get_recite(start_verse, start_verse))
        start_verse += 1

    return verses
    

