def quadratic_search(array, target):
    count = 0
    position = -1
    entered = False

    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] == target:
                if not entered:
                    position = i
                    if array[j] == target:
                        count += 1
            if count > 0:
                entered = True

    return position
