def binary_search(arr, target):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high)
        if arr[mid] == target:
            return mid
        elif arr[mid]>target:
            high = mid -1
        else:
            low = mid +1
        
arr = [10, 15, 20, 25, 30, 35]
target = 15
index = binary_search(arr, target)
if index != -1:
    print(f"element found at index {index}")
else:
    print("element not found")

# size = int(input("size: "))
# for i in range(1, size+1):
#     if i == 1 or i == size:
#         print("x" * size)
#     else:
#         print("x" + " " * (size-2) + "x")

# for i in range (5):
#     x = "*" * (2 * i + 1)
#     print(f"{x: ^10}")

# i = 5
# while i > 0:
#     x = "*" *(2 * i -1)
#     print(f"{x: ^10}")
#     i -= 1

     
