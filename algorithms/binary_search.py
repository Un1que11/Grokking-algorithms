def binary_search(sorted_list, value):
    first_item = 0
    last_item = len(sorted_list) - 1
    while first_item <= last_item:
        mid_item = (first_item + last_item) // 2
        guess = sorted_list[mid_item]
        if value < guess:
            last_item = mid_item - 1
        elif value > guess:
            first_item = mid_item + 1
        else:
            return mid_item
    return None
