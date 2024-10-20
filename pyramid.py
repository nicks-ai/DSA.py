# # pyramid
# for i in range(5):
#     x = "*" *(2 * i -1)
#     print(f"{x: ^10}")

# # inverted
# n = 5
# for i in range(n):
#     print(" " * i + "*" * (2*(n-i)-1))

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j]> array[j+1]: 
                array[j], array[j+1] = array[j+1], array[j]
    return array
array = [90, 10, 1]
print(f"unsorted array", array)
print(f"sorted array", bubble_sort(array))

n = 5
for i in range(n):
    print(" " * i + "*" *(2*(n-i)-1))