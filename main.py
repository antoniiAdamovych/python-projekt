def main():
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
        #getMedian()s
        pass
    else:
        print("Ungültige Auswahl!")

if __name__=="__main__":
    main()