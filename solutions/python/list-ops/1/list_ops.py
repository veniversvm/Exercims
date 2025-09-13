def append(list1, list2):
    if not list1:
        return list2
    len_list1 = len(list1)
    len_list2 = len(list2)
    new_list = [0] * (len_list2 + len_list1)

    for index, value in enumerate(list1):
        new_list[index] = value

    for index, value in enumerate(list2):
        new_list[len_list1 + index] = value
    return new_list


def concat(lists):
    new_list = []
    for element_lis in lists:
        for e in element_lis:
            new_list.append(e)
    return new_list


def filter(function, list):
    if not list:
        return []
    return [e for e in list if function(e)]


def length(list):
    count = 0
    for _ in list:
        count += 1
    return count


def map(function, list):
    if not list:
        return []
    return [function(e) for e in list ]


def foldl(function, list, initial):
    for e in list:
        initial = function(initial, e)
    return initial


def foldr(function, list, initial):
    for i in range(len(list) - 1, -1, -1):
        initial = function(initial, list[i])
    return initial


def reverse(list):
    new_list = []
    for element in list:
        new_list.insert(0, element)
    return new_list
        
