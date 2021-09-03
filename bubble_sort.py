def bubble_sort(arr):
    for i in range(len(arr)):
        for idx in range(len(arr) - i - 1):
            if arr[idx] > arr[idx+1]:
                temp = arr[idx]
                arr[idx] = arr[idx+1]
                arr[idx+1] = temp
    return arr

items = [123, 456, 93, 47, 13, 768, 987, 465]
bubble_lst = bubble_sort(items)
print('Bubble Sort: ' + str(bubble_lst))