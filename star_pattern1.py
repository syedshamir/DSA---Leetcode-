def triangle(n):
    for i in range(n):
        for j in range(i):
            print(j, end = " ")
        print()    

triangle(5)
