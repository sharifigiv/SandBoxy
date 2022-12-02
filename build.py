def build ():
    All = {}
    
    for i in range (25, 1680//5):
        for j in range (1, 1050//5):
            l = (i * 5, j * 5)

            All[l] = ('Null', True)

    return All
