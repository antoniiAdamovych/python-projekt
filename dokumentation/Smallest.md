### Dokumentation zum Code der smallest Funktion

#### Funktion: `getSmallestNumber`

**Beschreibung:**
Die Funktion `getSmallestNumber` ermittelt das kleinste Element in einer Liste von Zahlen.

**Parameter:**
- `lst` (List[float/int]): Eine Liste von numerischen Werten (Ganzzahlen oder Fließkommazahlen).

**Rückgabewert:**
- `float/int`: Das kleinste Element in der Liste.

**Funktionsweise:**
1. Die Funktion initialisiert die Variable `smallest` mit dem ersten Element der Liste `lst`.
2. Sie iteriert über jedes Element `x` in der Liste `lst`.
3. Innerhalb der Schleife wird überprüft, ob `x` kleiner ist als `smallest`.
4. Wenn ja, wird `smallest` auf den Wert von `x` aktualisiert.
5. Nach Abschluss der Schleife wird das kleinste Element zurückgegeben.

**Beispiel:**
```python
zahlen = [4, 23, 8, 13, 7, 9, 42, 11, 6, 80, 3]
print("Smallest number in list:", getSmallestNumber(zahlen))
```

**Erklärung des Hauptprogramms:**
Das Hauptprogramm testet die Funktion `getSmallestNumber` mit einer vordefinierten Liste von Zahlen.

**Vorgehen:**
1. Es wird eine Liste `zahlen` definiert, die mehrere numerische Werte enthält.
2. Die Funktion `getSmallestNumber` wird mit dieser Liste als Argument aufgerufen.
3. Das Ergebnis wird auf der Konsole ausgegeben.

**Beispiel:**
```python
zahlen = [4, 23, 8, 13, 7, 9, 42, 11, 6, 80, 3]
print("Smallest number in list:", getSmallestNumber(zahlen))
```

**Ausgabe:**
```
Smallest number in list: 3
```

**Programmablaufplan**

![Kleinster Wert](https://github.com/antoniiAdamovych/python-projekt/blob/main/bilder/Small.png)
