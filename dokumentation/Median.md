# Median Funktion

## Inhalte

1. Grundprinzip
2. Technische Umsetzung
3. Programmablaufsplan

## Grundprinzip

Um den Median einer Liste zu finden, müssen zwei Kriterien erfüllt sein:

1. Die Liste muss sortiert sein.
2. Die Länge der Liste muss bekannt sein.

Wenn beide Kriterien erfüllt sind, wird überprüft, ob die Länge der Liste gerade oder ungerade ist:

- Wenn die Länge der Liste ungerade ist, wird der Index des Medians durch die Division der Länge der Liste durch 2 (ohne Nachkommastellen) bestimmt. Der Wert an diesem Index ist der Median.
- Wenn die Länge der Liste gerade ist, wird der Median durch den Durchschnitt der beiden mittleren Werte der Liste berechnet.

## Technische Umsetzung

Zunächst gibt es keine Werte, deshalb müssen sie erst abgefragt werden. Dafür wurde die `RequestAnArray` erstellt, die in einer `while` Schleiche die Zahlen abliest.
Um die Eingabe der Werte zu beenden, muss eine `-1` eingegeben werden. Zusätzlich wird die Liste sofort nach der Beendung der Schleife sortiert und zurückgegeben.

Nachdem die Werte sortiert und übergeben wurden, wird die Länge der Liste abgelesen und neue Variable `median` definiert. Als nächstes wird überprüft, ob die Länge grade ist. Wenn ja, dann wir der Durchschnitt der beiden mittleren Werte berechnet:

```Python
if(length % 2 == 0):
    median = (array[length//2 - 1] + array[length//2]) / 2
```

Falls die Länge ungrade ist, wird sie durch 2 geteilt und der mittlere Wert wird zurüchgegeben:

```Python
median = array[length//2]
```

## Programmablaufplan

![Median Programmablaufplan](https://github.com/antoniiAdamovych/python-projekt/blob/main/bilder/Median.png)
