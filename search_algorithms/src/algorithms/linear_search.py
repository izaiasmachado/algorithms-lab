def linear_search_fast_return(array, target):
    for i, element in enumerate(array):
        if element == target:
            return i
    
    return -1

def linear_search_slow_return(array, element):
    element_index = -1

    for i, element in enumerate(array):
        if array[i] == element:
            element_index = i

    return element_index