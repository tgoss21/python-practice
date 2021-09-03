def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle_idx = len(arr) // 2
    left_split = arr[middle_idx:]
    right_split = arr[:middle_idx]
    
    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)
    
    return merge(left_sorted, right_sorted)
    

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    if left:
        result += left
    if right:
        result += right
    return result



items1 = [123, 456, 93, 47, 13, 768, 987, 465]
merge_lst = merge_sort(items1)
print('Merge Sort: ' + str(merge_lst))

