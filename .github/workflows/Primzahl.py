while True:
    Dividend = 2
    Rest = 0
    Eingabe = 0
    print("Eine Primzahl ist eine Zahl, welche sich nur durch 1 und durch sich selbst teilen lässt.")
    print("0, 1 und 2 werden nicht als Primzahlen gezählt, daher sind solche Eingaben ungültig.")
    print(" ")

    while Eingabe < 3:
        Eingabe = int(input("Welche Zahl soll überprüft werden? "))

    while Dividend <= Eingabe // 2:  # Nur bis zur Hälfte der Eingabe prüfen
        if Eingabe % Dividend == 0:
            Rest += 1
            break  # Sobald ein Teiler gefunden wird, abbrechen
        Dividend += 1

    print(" ")

    if Rest == 0:  # Wenn Rest == 0, dann ist die Zahl prim
        print(f"Die Zahl {Eingabe} ist eine Primzahl.")
    else:
        print(f"Die Zahl {Eingabe} ist keine Primzahl.")

    print(" ")

    if input("Neue Berechnung durchführen? (Ja/Nein) ").lower() != "ja":
        break






        