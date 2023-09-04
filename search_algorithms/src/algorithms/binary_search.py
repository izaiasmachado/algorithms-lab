# create function to call binary search with first element

def binary_search(array, target):
    return bs(target, array, 0, len(array) - 1)

def bs(x, v, e, d):
    meio = (e + d) // 2
    if v[meio] == x:
        return meio
    if e >= d:
        return -1
    elif v[meio] < x:
        return bs(x, v, meio + 1, d)
    else:
        return bs(x, v, e, meio - 1)
