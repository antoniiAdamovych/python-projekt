from functions.median import getMedian
from functions.smallest import getSmallestNumber
from functions.biggest import getBiggestNumber
from functions.average import getListAverage
from functions.sum import getNumbersSum
from functions.sortList import quickSort

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    FAIL = '\033[91m'

def main():
    print("")
    
    print(bcolors.OKGREEN + "Willkommen in unserem Programm!" + bcolors.ENDC)

    print("")
    
    print("Bitte wählen Sie eine der folgenden Funktionen:")
    
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
    
    auswahl = 0
    while True:
        try:
            auswahl = int(input("Geben Sie die Nummer der gewünschten Finktion ein (-1 für Beenden): "))
            break
        except:
            print("")
            print(bcolors.FAIL + 'Ungültige Eingabe' + bcolors.ENDC)
            print("")
            continue
    
    print("")
    print("---------------------")
    print("")
    
    array = RequestAnArray()
    
    if auswahl == 1:
        print("Kleinster Wert: " + str(getSmallestNumber(array)))
        pass
    elif auswahl == 2:
        print("Größter Wert: " + str(getBiggestNumber(array)))
        pass
    elif auswahl == 3:
        print("Summe aller Zahlen: " + str(getNumbersSum(array)))
        pass
    elif auswahl == 4:
        print("Durchschnitt: " + str(getListAverage(array)))
        pass
    elif auswahl == 5:
        print("Sortierte Liste: " + str(quickSort(array, 0, len(array)-1)))
        pass
    elif auswahl == 6:
        print("Median: " + str(getMedian(array)))
        pass
    else:
        print("Ungültige Auswahl!")
        
# Die Werte werden in einem Array gespeichert und sortiert
def RequestAnArray():
    array = []
    index = 1
    print('Geben Sie die Zahlen ein (-1 für Beenden):')
    while True:
        num = 0
        
        try: 
            num = int(input(str(index) + '. '))
        except:
            print("")
            print(bcolors.FAIL + 'Ungültige Eingabe' + bcolors.ENDC)
            print("")
            continue
        
        if(num <= -1):
            break
        
        array.append(num)
        index += 1

    return array

if __name__=="__main__":
    main()
    