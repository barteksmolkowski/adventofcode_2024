import sys

# Wczytaj dane
dane = sys.stdin.read().strip().split("\n")
for i in range(len(dane)):
    dane[i] = dane[i].split("-")  # Poprawienie przypisania
print(dane)

# Tworzymy słownik elementów
elementy = {}
for i in range(len(dane)):
    for j in range(len(dane[i])):
        element = dane[i][j]
        if element not in elementy:
            elementy[element] = []  # Tworzymy nową listę dla elementu
        # Dodajemy połączenia dla elementu
        druga_strona = dane[i][1 - j]  # Pobieramy przeciwległy element z pary
        if druga_strona not in elementy[element]:
            elementy[element].append(druga_strona)

# Wyświetlenie wyników
for klucz, wartosci in elementy.items():
    print(f"{klucz}: {wartosci}")
