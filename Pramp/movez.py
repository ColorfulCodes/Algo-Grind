def move(a):
    write = 0
    for i in range(len(a)):
        if a[i] != 0:
            a[write]= a[i]
            write += 1
    for j in range(write,len(a)):
        a[j] = 0

move([1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0])
