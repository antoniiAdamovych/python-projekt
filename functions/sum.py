def getNumbersSum(lst):
    sum = 0
    for x in lst:
        sum += x
    return sum

if __name__ == "__main__":
    zahlen = [4, 23, 8, 13, 7, 9, 42, 11, 6, 80, 3]
    print("Sum of numbers in list:", getNumbersSum(zahlen))

