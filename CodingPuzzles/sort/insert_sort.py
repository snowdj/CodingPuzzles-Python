# Insertion Sort

def InsertionSort(lst):
    for j in range(1, len(lst)):
        key = lst[j]
        i = j - 1
        while i >= 0 and lst[i] > key:
            lst[i+1] = lst[i]
            i = i - 1
        lst[i+1] = key

if __name__ == '__main__':
    input_list = []
    input = raw_input('Please input numbers to be sorted, separate by space:')
    for item in input.split(' '):
        input_list.append(int(item))

InsertionSort(input_list)
print(input_list)
