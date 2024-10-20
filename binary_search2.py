def binary_search(arr, target):
    low = 0
    high = len(arr) -1
    while low <= high:
        mid = (low + high)
        if arr[mid] == target:
            return mid
        elif arr [mid] > target:
            high = mid -1
        else:
            low = mid +1
arr = [5, 2, 1, 4, 3]
target = 1
index = binary_search(arr, target)
if target != -1:
    print(f"element found at index{index}")
else:
    print("element not found")
      