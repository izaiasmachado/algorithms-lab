def cubic_search(array, target):
    posicao = -1
    size_array = len(array)

    for i in range(size_array):
        for j in range(size_array):
            for k in range(size_array):
                if array[i] == target and array[j] == target and array[k] == target:
                    posicao = i

    return posicao