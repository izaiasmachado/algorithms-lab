def ternary_search(array, target):
    start = 0
    end = len(array) - 1
    
    while start <= end:
        left_third = start + (end - start) // 3
        right_third = end - (end - start) // 3
        
        if array[left_third] == target:
            return left_third
        elif array[right_third] == target:
            return right_third
        elif array[left_third] > target:
            end = left_third - 1
        elif array[right_third] < target:
            start = right_third + 1
        else:
            start = left_third + 1
            end = right_third - 1

    return -1
