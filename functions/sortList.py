def partition(array, von, bis):
    pivot = array[von]      # "Pivot" als erstes Element der Liste
    i = von + 1             # Zähler "i" der eins nach dem Pivot starten
    j = bis                 # Zähler "j" der das letzte Element ist

    # Solange die beiden Zähler sich nicht begegnet sind, wird versucht die
    # Elemente der Liste aufzuteilen in links (kleiner) und rechts (größer)
    while i<=j:
        # Solange i <= j und das Element an Stelle "i" kleiner als Pivot ist muss aufgerückt werden 
        while i <= j and array[i] < pivot:
            i += 1
        # Solange i <= j und das Element an Stelle "j" größer oder gleich dem Pivot ist muss aufgerückt werden
        while i <= j and array[j] >= pivot:
            j -= 1
        # Wenn die beiden Zähler sich nicht überholt haben, dann Normaltauscht der beiden Elemente der Zähler
        if i <= j:
            temp = array[i]         
            array[i] = array[j]
            array[j] = temp
            i += 1
            j += 1

    # Nachdem die Zähler sich überholt haben, muss der Pivottausch stattfinden
    # Hier nutzt man den Zähler "i-1", um sicher zu gehen, dass die Elemente
    # nicht versehentlich in den falschen Teil geschoben werden
    temp = array[i-1]
    array[i-1] = pivot
    array[von] = temp

    # Zurückgeben der Position von dem aktuellen Pivot-Element
    return i-1

def quickSort(array, von, bis):
    # Rekursions abbruch
    if von < bis:
        # Sucht die Position des Pivot-Elementes, um nachher die Listen zu teilen
        positionPivot = partition(array, von, bis)
        # Rekursion für den linken Teil der Liste, also "von" bis "Pivot - 1", minus weil Pivot bereits sortiert ist
        quickSort(array, von, positionPivot - 1)
        # Rekursion für den rechten Teil der Liste, also "Pivot + 1" bis "bis", plus weil Pivot bereits sortiert ist
        quickSort(array, positionPivot + 1, bis)

if __name__=="__main__":
    array = [1, 12, 18, 2, 8, 11, 12, 0, 10, 9, 22, 13, 3, 7, 4, 15, 16, 20]
    print(array)
    quickSort(array, 0, len(array)-1)
    print(array)