# Quick Sort

def QuickSort(lst):
    if lst is None or len(lst) <= 1:
        return lst

    pivot = lst[0]
    # Partition
    left = [x for x in lst[1:] if x < pivot]
    right = [x for x in lst[1:] if x >= pivot]
    result = QuickSort(left) + [pivot] + QuickSort(right)
    return result