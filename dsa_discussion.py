# DSA_3

def interactive_binary(arr, target):

    high = len(arr) - 1
    low = 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid]> target:
            high = mid -1
        else :
            low = mid +1


    return -1 

arr = [1, 2, 3, 4, 5]
target = 1

print(interactive_binary(arr, target))



#  

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = node(1)
head.next = node (2)
head.next.next = node (3)
head.next.next.next = node (4)

current = head
while current:
    print (current.data, end= " ")
    current = current.next


#DSA_5 RECURSION
gago_joshua = 6
utot = 5
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n -1)
    
print(factorial(gago_joshua))




