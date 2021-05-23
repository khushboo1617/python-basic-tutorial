def sum(x, *y) : # *y can have multiple value.
    print(x)
    print(y)
    a = x
    for i in y:
        b= a+ i
        print(b)
        

sum(3,5,6,7)
