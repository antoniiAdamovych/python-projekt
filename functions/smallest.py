def getSmallestNumber(lst):
    smallest = lst[0]
    for x in lst:
        if smallest > x:
            smallest = x
    return smallest

if __name__ == "__main__":
    zahlen = [4, 23, 8, 13, 7, 9, 42, 11, 6, 80, 3]
    print("Smallest number in list:", getSmallestNumber(zahlen))
