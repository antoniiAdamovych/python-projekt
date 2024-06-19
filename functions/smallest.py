def getSmallestNumber(lst):
    smallest = lst[0]
    for x in lst:
        if smallest > x:
            smallest = x
    return smallest
