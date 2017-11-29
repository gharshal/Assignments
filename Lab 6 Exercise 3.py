def first_neg(x):
    i = 0
    while i < len(x):
        i = i + 1
        if x[i-1]<0:
            print(i-1)
            break
    else:
        return
