### Dokumentation zum Code der Average Funktion

#### Funktion: `getListAverage`

**Beschreibung:**
Die Funktion `getListAverage` berechnet den Durchschnitt (arithmetisches Mittel) einer Liste von Zahlen und rundet das Ergebnis auf zwei Dezimalstellen.

**Parameter:**
- `lst` (List[float/int]): Eine Liste von numerischen Werten (Ganzzahlen oder Fließkommazahlen).

**Rückgabewert:**
- `float`: Der auf zwei Dezimalstellen gerundete Durchschnitt der Zahlen in der Liste.

**Funktionsweise:**
1. Die Funktion initialisiert die Variable `sum` mit dem Wert 0.
2. Sie iteriert über jedes Element `x` in der Liste `lst` und addiert `x` zu `sum`.
3. Nachdem die Schleife abgeschlossen ist, wird der Durchschnitt berechnet, indem `sum` durch die Anzahl der Elemente in `lst` (`len(lst)`) geteilt wird.
4. Der Durchschnittswert wird auf zwei Dezimalstellen gerundet und zurückgegeben.

**Beispiel:**
```python
zahlen = [4, 23, 8, 13, 7, 9, 42, 11, 6, 80, 3]
print("Number average of list:", getListAverage(zahlen))
```

#### Hauptprogramm

**Beschreibung:**
Das Hauptprogramm testet die Funktion `getListAverage` mit einer vordefinierten Liste von Zahlen.

**Vorgehen:**
1. Es wird eine Liste `zahlen` definiert, die mehrere numerische Werte enthält.
2. Die Funktion `getListAverage` wird mit dieser Liste als Argument aufgerufen.
3. Das Ergebnis wird auf der Konsole ausgegeben.

**Beispiel:**
```python
zahlen = [4, 23, 8, 13, 7, 9, 42, 11, 6, 80, 3]
print("Number average of list:", getListAverage(zahlen))
```

**Ausgabe:**
```
Number average of list: 18.18
```
