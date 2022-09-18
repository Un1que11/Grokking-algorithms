def qsort(array):
    if len(array) < 2:
        return array
    else:
        support_element = array[0]
        less_support_element = [i for i in array[1:] if i <= support_element]
        over_support_element = [i for i in array[1:] if i > support_element]
        return qsort(less_support_element) + [support_element] + qsort(over_support_element)
