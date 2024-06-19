### Dokumentation zum Code der Sum Funktion

#### Funktion: `getNumbersSum`

**Beschreibung:**
Die Funktion `getNumbersSum` berechnet die Summe aller Zahlen in einer gegebenen Liste.

**Parameter:**
- `lst` (List[float/int]): Eine Liste von numerischen Werten (Ganzzahlen oder Fließkommazahlen).

**Rückgabewert:**
- `float/int`: Die Summe der Zahlen in der Liste.

**Funktionsweise:**
1. Die Funktion initialisiert die Variable `sum` mit dem Wert 0.
2. Sie iteriert über jedes Element `x` in der Liste `lst` und addiert `x` zu `sum`.
3. Nachdem die Schleife abgeschlossen ist, wird die Gesamtsumme zurückgegeben.

**Beispiel:**
```python
zahlen = [4, 23, 8, 13, 7, 9, 42, 11, 6, 80, 3]
print("Sum of numbers in list:", getNumbersSum(zahlen))
```

#### Hauptprogramm

**Beschreibung:**
Das Hauptprogramm testet die Funktion `getNumbersSum` mit einer vordefinierten Liste von Zahlen.

**Vorgehen:**
1. Es wird eine Liste `zahlen` definiert, die mehrere numerische Werte enthält.
2. Die Funktion `getNumbersSum` wird mit dieser Liste als Argument aufgerufen.
3. Das Ergebnis wird auf der Konsole ausgegeben.

**Beispiel:**
```python
zahlen = [4, 23, 8, 13, 7, 9, 42, 11, 6, 80, 3]
print("Sum of numbers in list:", getNumbersSum(zahlen))
```

**Ausgabe:**
```
Sum of numbers in list: 206
```

## Programmablaufplan

![Median Programmablaufplan](https://github.com/antoniiAdamovych/python-projekt/blob/main/bilder/Sum.png)
