def sum_odd_while_v2(n):
    '''(int)->int
Returns the sum of all odd integers between 5 and n'''
    x = 0
    i = 5
    while i <= n:
        x = x + i
        i = i + 2
        print((x))
