def getMedian(array):
    # Die Funktion RequestAnArray() wird aufgerufen und das Array wird in der Variable array gespeichert
    length = len(array)
    median = 0
    
    if(length % 2 == 0):
        # Wenn die Länge des Arrays gerade ist, wird der Median berechnet, indem die beiden mittleren Zahlen addiert und durch 2 geteilt werden
        median = (array[length//2 - 1] + array[length//2]) / 2
    else:
        # Wenn die Länge des Arrays ungerade ist, wird der Median die mittlere Zahl
        median = array[length//2]
        
    print('Median:', median)
    return median
        

if __name__=="__main__":
    getMedian()