from functions.median import getMedian
<<<<<<< HEAD
from functions.sortList import quickSort

=======
from functions.smallest import getSmallestNumber
from functions.biggest import getBiggestNumber
from functions.average import getListAverage
from functions.sum import getNumbersSum
from functions.sortList import getSortList
>>>>>>> d9fd65091b111e57acec478d646a92a7c3613dcc
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
        getSmallestNumber()
        pass
    elif auswahl == 2:
        getBiggestNumber
        pass
    elif auswahl == 3:
        getNumbersSum()
        pass
    elif auswahl == 4:
        getListAverage
        pass
    elif auswahl == 5:
<<<<<<< HEAD
        quickSort(array, 0, len(array)-1)
=======
        getSortList()
>>>>>>> d9fd65091b111e57acec478d646a92a7c3613dcc
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

    return array

if __name__=="__main__":
    main()
    