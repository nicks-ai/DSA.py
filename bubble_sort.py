def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
    return arr

arr = [9, 5, 10 , 8, 4, 1, 2, 7, 6, 3]
print("original array", arr)
sorted_array = bubble_sort(arr)
print("sorted", sorted_array) 


