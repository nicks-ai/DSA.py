def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [ x for x in arr if x < pivot]
    middle = [ x for x in arr if x == pivot]
    right = [ x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [100, -1, 388, 483, 8, 724, 10, 90, 7427]
print(quick_sort(arr))


