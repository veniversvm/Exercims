def is_in_list(search_list: list, value: int):
    len_list = len(search_list)
    if   len_list == 1 and search_list[0] != value:
        return False
    half = round(len_list / 2)
    if search_list[half] == value:
        return True
    if value > search_list[half]:
        return is_in_list(search_list[half:], value)
    else:
        return is_in_list(search_list[:half], value)

def find(search_list: list, value: int):
    len_list = len(search_list)
    if len_list and search_list[0] == value:
        return 0

    if len_list and is_in_list(search_list, value):
        return search_list.index(value)
    raise ValueError("value not in array")
