def recursive_bubble_sort (arr, n=None):
    if n is None:
        n = len(arr)
    if n == 0:
        return
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    recursive_bubble_sort(arr, n-1)

arr=[3, 1, 4, 5, 2]
print(arr)
recursive_sort = recursive_bubble_sort(arr)
print(arr)
