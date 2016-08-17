# Bubble Sort

def BubbleSort(lst):
    if lst is None or len(lst) <= 1:
        return lst

    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] > lst[j]:
                lst[j] = lst[i]

    return lst
