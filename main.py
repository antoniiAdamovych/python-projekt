from functions.median import getMedian

def main():
    array = RequestAnArray()
    
    print("Willkommen! Bitte wählen Sie eine Figur für die Flächenberechnung:")
    print("1. Kleinster Wert")
    print("2. Größter Wert")
    print("3. Summe aller Zahlen")
    print("4. Durchschnitt berechnen")
    print("5. Liste Sortieren")
    print("6. Median ausgeben")
    
    auswahl = int(input("Geben Sie die Nummer der gewünschten Figur ein: "))
    
    if auswahl == 1:
        #getSmallestNumber()
        pass
    elif auswahl == 2:
        #getBiggestNumber
        pass
    elif auswahl == 3:
        #getNumbersSum()
        pass
    elif auswahl == 4:
        #getListAverage
        pass
    elif auswahl == 5:
        #getSortList()
        pass
    elif auswahl == 6:
        getMedian(array)
        pass
    else:
        print("Ungültige Auswahl!")
        
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
    main()
    