# Merge Sort

def MergeSort(lst):
    if lst is None or len(lst) <= 1:
        return lst

    def merge(left, right):
        merged = []
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))

        if len(left) > 0:
            merged += left
        if len(right) > 0:
            merged += right

        return merged

    pivot = len(lst)/2
    res = merge(MergeSort(lst[:pivot]), MergeSort(lst[pivot:]))
    return res