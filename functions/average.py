def getListAverage(lst):
    sum = 0
    for x in lst:
        sum += x
    average = sum / len(lst)
    return round(average, 2)

if __name__ == "__main__":
    zahlen = [4, 23, 8, 13, 7, 9, 42, 11, 6, 80, 3]
    print("Number average of list:", getListAverage(zahlen))


