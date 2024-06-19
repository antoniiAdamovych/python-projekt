def getBiggestNumber(lst):
    biggest = lst[0]
    for x in lst:
        if biggest < x:
            biggest = x
    return biggest
if __name__=="__main__":
    zahlen = [4, 23, 8, 13, 7, 9, 42, 11, 6, 80, 3]
    print("Biggest number in list:", getBiggestNumber(zahlen))
