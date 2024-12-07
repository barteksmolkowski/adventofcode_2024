import numpy as np

# Rozmiar tablicy
x = 7
y = 7

# Tworzymy tablicę z wieloma wystąpieniami słowa "xmas"
tablica = np.array([
    ['x', 'm', 'a', 's', 'x', 'm', 'a'],
    ['m', 'x', 'm', 'a', 's', 'x', 'm'],
    ['a', 'a', 'x', 'm', 'a', 's', 'x'],
    ['s', 'm', 'a', 'm', 'x', 'm', 'a'],
    ['m', 'a', 's', 'x', 'm', 'a', 's'],
    ['a', 's', 'x', 'm', 'a', 's', 'x'],
    ['s', 'x', 'm', 'a', 's', 'x', 'm']
])

# Słowo, które chcemy znaleźć
slowa = ["xmas"]

# Kierunki (z numerami i nazwami)
kierunki = {
    1: (0, 1),   # prawo
    2: (0, -1),  # lewo
    3: (1, 0),   # dół
    4: (-1, 0),  # góra
    5: (1, 1),   # prawy dolny skos
    6: (-1, -1), # lewy górny skos
    7: (1, -1),  # lewy dolny skos
    8: (-1, 1)   # prawy górny skos
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

# Funkcja do sprawdzenia, czy słowo występuje w danym kierunku
def sprawdz_slowo(tablica, slowo, kierunek):
    wystapienia = []  # Lista do przechowywania wystąpień
    for i in range(tablica.shape[0]):
        for j in range(tablica.shape[1]):
            a, b = kierunki[kierunek]
            if 0 <= i + a * (len(slowo) - 1) < tablica.shape[0] and 0 <= j + b * (len(slowo) - 1) < tablica.shape[1]:
                # Inicjalizujemy zmienne
                znaleziono = True
                nowe_slowo = ""
                for litera in range(len(slowo)):
                    x = i + a * litera
                    y = j + b * litera
                    if tablica[x, y] != slowo[litera]:
                        znaleziono = False
                        break
                    nowe_slowo += tablica[x, y]
                if znaleziono:
                    wystapienia.append((i, j))  # Dodajemy początkowe współrzędne
    return wystapienia

# Sprawdzamy wszystkie kierunki
for slowo in slowa:
    for kierunek in kierunki:
        wystapienia = sprawdz_slowo(tablica, slowo, kierunek)
        if wystapienia:
            print(f"Słowo '{slowo}' znaleziono w kierunku '{kierunki_nazwy[kierunek]}': {wystapienia}")
