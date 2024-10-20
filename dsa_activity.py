def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:               
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:  
            break
    return arr


def binary_search(arr, target, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, low, mid - 1)     
        else:
            return binary_search(arr, target, mid + 1, high)
    else:
        return -1



if __name__ == "__main__":
    # Bubble Sort
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    sorted_arr = bubble_sort(arr)
    print("Sorted array:", sorted_arr)

    # Recursive Binary Search
    target = 22
    result = binary_search(sorted_arr, target, 0, len(sorted_arr) - 1)
    
    if result != -1:
        print(f"Element {target} is present at index {result}.")
    else:
        print(f"Element {target} is not present in the array.")
