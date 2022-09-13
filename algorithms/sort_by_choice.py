def find_smallest_item(array):
    smallest_value = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest_value:
            smallest_value = array[i]
            smallest_index = i
    return smallest_index


def selection_sort(array):
    new_array = []
    for i in range(len(array)):
        smallest = find_smallest_item(array)
        new_array.append(array.pop(smallest))
    return new_array
