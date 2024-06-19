### Dokumentation zum Code der QuickSort Funktion

#### Funktion: `partition`

**Beschreibung:**
Die Funktion `partition` teilt eine gegebene Liste in zwei Teile, basierend auf einem Pivot-Element. Alle Elemente, die kleiner als das Pivot-Element sind, werden auf die linke Seite gestellt, während die größeren Elemente auf die rechte Seite kommen.

**Parameter:**
- `array` (List[float/int]): Eine Liste von numerischen Werten (Ganzzahlen oder Fließkommazahlen).
- `von` (int): Der Startindex des zu partitionierenden Abschnitts.
- `bis` (int): Der Endindex des zu partitionierenden Abschnitts.

**Rückgabewert:**
- `int`: Die neue Position des Pivot-Elements.

**Funktionsweise:**
1. Das erste Element der Liste wird als Pivot gewählt.
2. Zwei Zeiger `i` und `j` werden initialisiert. `i` startet direkt nach dem Pivot, und `j` am Ende der Liste.
3. Die Zeiger bewegen sich durch die Liste: `i` sucht ein Element, das größer oder gleich dem Pivot ist, und `j` sucht ein Element, das kleiner als das Pivot ist.
4. Wenn `i` und `j` beide passende Elemente gefunden haben und sich noch nicht überholt haben, tauschen sie diese Elemente aus.
5. Nachdem sich die Zeiger überholt haben, wird das Pivot-Element an seine endgültige Position gebracht.
6. Die Funktion gibt die neue Position des Pivot-Elements zurück.

**Beispiel:**
```python
array = [34, 7, 23, 32, 5, 62]
pivot_position = partition(array, 0, len(array) - 1)
print("Pivot is now at position:", pivot_position)
print("Array after partitioning:", array)
```

#### Funktion: `quickSort`

**Beschreibung:**
Die Funktion `quickSort` sortiert eine gegebene Liste von numerischen Werten mithilfe des QuickSort-Algorithmus.

**Parameter:**
- `array` (List[float/int]): Eine Liste von numerischen Werten (Ganzzahlen oder Fließkommazahlen).
- `von` (int): Der Startindex des zu sortierenden Abschnitts.
- `bis` (int): Der Endindex des zu sortierenden Abschnitts.

**Rückgabewert:**
- `None`: Die Funktion gibt keinen Wert zurück, sondern sortiert die Liste in-place.

**Funktionsweise:**
1. Die Funktion überprüft, ob der Startindex kleiner als der Endindex ist.
2. Sie ruft die `partition`-Funktion auf, um die Liste zu teilen und die Position des Pivot-Elements zu finden.
3. Sie ruft sich rekursiv für die linken und rechten Teilabschnitte der Liste auf, um diese ebenfalls zu sortieren.

**Beispiel:**
```python
array = [34, 7, 23, 32, 5, 62]
quickSort(array, 0, len(array) - 1)
print("Sorted array:", array)
```

#### Hauptprogramm

**Beschreibung:**
Das Hauptprogramm testet die Funktion `quickSort` mit einer vordefinierten Liste von Zahlen.

**Vorgehen:**
1. Es wird eine Liste `zahlen` definiert, die mehrere numerische Werte enthält.
2. Die Funktion `quickSort` wird mit dieser Liste als Argument aufgerufen.
3. Das Ergebnis wird auf der Konsole ausgegeben.

**Beispiel:**
```python
zahlen = [34, 7, 23, 32, 5, 62]
quickSort(zahlen, 0, len(zahlen) - 1)
print("Sorted array:", zahlen)
```

**Ausgabe:**
```
Sorted array: [5, 7, 23, 32, 34, 62]
```

### Struktogramm
![QuickSort Struktogramm](https://github.com/antoniiAdamovych/python-projekt/blob/main/bilder/Sort.png)