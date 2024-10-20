size = int(input("size: "))

for i in range(size):
    print("x " * size)


for i in range(size):

    for j in range(size):
        if j % 2 == 0:
            print("o ", end="")
        else:
            print("x ", end="")
    print()
print()

for i in range(size):
    if i % 2 == 0:
        print("o " * size)
    else:
        print("x " * size)
print()

for i in range(size):

    for j in range(size):
        if i % 2 == 0:
            if j % 2 == 0:
                print("o ", end="")
            else:
                print("x ", end="")
        else:
            if j % 2 == 1:
                print("o ", end="")
            else:
                print("x ", end="")
            
    print()
print()