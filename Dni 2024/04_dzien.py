import numpy as np

x = 7
y = 7

tablica = np.array([
    ['x', 'm', 'a', 's', 'x', 'm', 'a'],
    ['m', 'x', 'm', 'a', 's', 'x', 'm'],
    ['a', 'a', 'x', 'm', 'a', 's', 'x'],
    ['s', 'm', 'a', 'm', 'x', 'm', 'a'],
    ['m', 'a', 's', 'x', 'm', 'a', 's'],
    ['a', 's', 'x', 'm', 'a', 's', 'x'],
    ['s', 'x', 'm', 'a', 's', 'x', 'm']
])

slowa = ["xmas"]

kierunki = {
    1: (0, 1),
    2: (0, -1),
    3: (1, 0),
    4: (-1, 0),
    5: (1, 1),
    6: (-1, -1),
    7: (1, -1),
    8: (-1, 1)
}

kierunki_nazwy = {
    1: "prawo",
    2: "lewo",
    3: "dół",
    4: "góra",
    5: "prawy dolny skos",
    6: "lewy górny skos",
    7: "lewy dolny skos",
    8: "prawy górny skos"
}

def sprawdz_czy_miejsce(i, j, a, b, slowo, tablica):
    for litera in range(len(slowo)):
        x = i + a * litera
        y = j + b * litera
        if tablica[x, y] != slowo[litera]:
            return False
    return True

def sprawdz_slowo(tablica, slowo, kierunek):
    wystapienia = []
    for i in range(tablica.shape[0]):
        for j in range(tablica.shape[1]):
            a, b = kierunki[kierunek]
            if 0 <= i + a * (len(slowo) - 1) < tablica.shape[0] and 0 <= j + b * (len(slowo) - 1) < tablica.shape[1]:
                if sprawdz_czy_miejsce(i, j, a, b, slowo, tablica):
                    wystapienia.append((i, j))
    return wystapienia

for slowo in slowa:
    for kierunek in kierunki:
        wystapienia = sprawdz_slowo(tablica, slowo, kierunek)
        if wystapienia:
            print(f"Słowo '{slowo}' znaleziono w kierunku '{kierunki_nazwy[kierunek]}': {wystapienia}")
