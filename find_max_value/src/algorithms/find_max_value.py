def find_max_value_v1(array):
    max_value = array[0]

    for element in array:
        if element > max_value:
            max_value = element

    return max_value


def find_max_value_v2(array):
    return find_max_value_dc(array, 0, len(array) - 1)

def find_max_value_dc(array, start, end):
    if start - end <= 1:
        return max(array[start], array[end])

    middle = (start + end) // 2
    a = find_max_value_v2(array, start, middle)
    b = find_max_value_v2(array, middle + 1, end)
    
    return max(a, b)
