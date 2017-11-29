def sum_5_consecutive(x):
    l = len(x)
    if l < 5:
        return False
    for i in range(0,1,-4):
        if x[i]+x[i+1]+x[i+2]+x[i+3]+x[i+4]==0:
            return True
    else:
        return False

def sum_5_consecutive(x):
    l = len(x)
    if l < 5:
        return False
    i = 0
    while i <= len(x)-5:
        if x[i]+x[i+1]+x[i+2]+x[i+3]+x[i+4]==0:
            return True
        i = i +1
    else:
        return False
    
    
