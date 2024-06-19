from functions.median import getMedian
from functions.sortList import quickSort

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

def main():
    print("")
    
    print(bcolors.OKGREEN + "Willkommen in unserem Programm!" + bcolors.ENDC)

    print("")
    
    print("Bitte wählen Sie eine der folgenden Finktionen:")
    
    print("")
    
    print("1. Kleinster Wert")
    print("2. Größter Wert")
    print("3. Summe aller Zahlen")
    print("4. Durchschnitt berechnen")
    print("5. Liste Sortieren")
    print("6. Median ausgeben")
    
    print("")
    print("---------------------")
    print("")
    
    auswahl = int(input("Geben Sie die Nummer der gewünschten Figur ein: "))
    
    print("")
    print("---------------------")
    print("")
    
    array = RequestAnArray()
    
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
        quickSort(array, 0, len(array)-1)
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
    