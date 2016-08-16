# Insertion Sort

def InsertionSort(lst):
    if lst is None or len(lst) == 0:
        return lst

    for j in range(1, len(lst)):
        key = lst[j]
        i = j - 1
        while i >= 0 and lst[i] > key:
            lst[i+1] = lst[i]
            i = i - 1
        lst[i+1] = key

    return lst
