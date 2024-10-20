def recursive_binary_search(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return recursive_binary_search(arr, low, mid -1, target)
    else:
        return recursive_binary_search(arr, mid +1, high, target)
    
arr = [ 90, 6, 5, 11, 10, 9, 1]
target = 90
low = 0
high = len(arr) -1
index = recursive_binary_search(arr, low, high, target)
if index != -1:
    print(f"index foud at {index}")
else:
    print("index not found")