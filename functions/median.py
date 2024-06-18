def getMedian():
    # Die Funktion RequestAnArray() wird aufgerufen und das Array wird in der Variable array gespeichert
    array = RequestAnArray()
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

    
# Die Werte werden in einem Array gespeichert und sortiert
def RequestAnArray():
    array = []
    index = 1
    print('Geben Sie die Zahlen ein (-1 für beenden):')
    while True:
        num = int(input(str(index) + '. '))
        
        if(num <= -1):
            break
        
        array.append(num)
        index += 1
    
    array.sort()
    return array
        

if __name__=="__main__":
    getMedian()