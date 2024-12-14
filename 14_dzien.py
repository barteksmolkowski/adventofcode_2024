import numpy as np

tablica = [
    "p=0,4 v=3,-3",
    "p=6,3 v=-1,-3",
    "p=10,3 v=-1,2",
    "p=2,0 v=2,-1",
    "p=0,0 v=1,3",
    "p=3,0 v=-2,-2",
    "p=7,6 v=-1,-3",
    "p=3,0 v=-1,-2",
    "p=9,3 v=2,3",
    "p=7,3 v=-1,2",
    "p=2,4 v=2,-3",
    "p=9,5 v=-3,-3"
]

liczby = []

for wiersz in tablica:
    liczba = ""

    for znak in wiersz:
        if znak.isdigit() or znak == "-":
            liczba += znak

        elif liczba:
            liczby.append(int(liczba))
            liczba = ""

    if liczba:
        liczby.append(int(liczba))

print(liczby)

szerokosc, wysokosc = 101, 103
wspolrzedne = []
wiersz = 0

while wiersz < (len(liczby) // 4):
    x_pocz = liczby[wiersz * 4]
    y_pocz = liczby[wiersz * 4 + 1]
    x_predkosc = liczby[wiersz * 4 + 2]
    y_predkosc = liczby[wiersz * 4 + 3]

    x_nowe = (x_pocz + 100 * x_predkosc) % szerokosc
    y_nowe = (y_pocz + 100 * y_predkosc) % wysokosc

    wspolrzedne.append((x_nowe, y_nowe))
    wiersz += 1

print(wspolrzedne)
