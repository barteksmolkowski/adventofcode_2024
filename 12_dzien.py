tablica = [
    "RGGGIICCFF",
    "RLLRIICCCF",
    "VVRRRCCFFF",
    "VVRCCCJFFF",
    "VVVVCJJCFE",
    "VVIVCCJJEE",
    "VVIIICJJEE",
    "MIPPIIJJEE",
    "MIIISISEEE",
    "XDMISSJEOO"
]

kierunki = {1: (0, -1), 2: (1, 0), 3: (0, 1), 4: (-1, 0)}

def jaki_elem(x, y):
    liczba = 0  # Inicjalizacja zmiennej liczba
    klucz = tablica[x][y]
    for i in range(1, 5):
        a, b = kierunki[i]

        # Sprawdzamy, czy sąsiad jest w tablicy i ma taki sam klucz
        if 0 <= x + a < len(tablica) and 0 <= y + b < len(tablica[0]) and tablica[x + a][y + b] == klucz:
            liczba += 1

    return klucz, liczba  # Zwracamy klucz oraz liczbę sąsiadów

elementy = {}

for i in range(len(tablica)):
    for j in range(len(tablica[i])):
        # Zakładając, że 'jaki_elem' zwraca (klucz, liczba_sasiadow)
        klucz, liczba = jaki_elem(i, j)
        
        # Tworzymy listę dla nowych kluczy
        if klucz not in elementy:
            elementy[klucz] = {'obwod': 0, 'pola': 0}
        
        # Obliczamy obwód jako 4 - liczba_sasiadów
        obwod = 4 - liczba
        elementy[klucz]['obwod'] += obwod
        elementy[klucz]['pola'] += 1

# Debugowanie: Drukowanie obwodów i liczby pól dla każdej litery
obwody = []
for klucz, dane in elementy.items():
    obwod_pomnozony = dane['obwod'] * dane['pola']
    print(f"Litera: {klucz} Obwody: {dane['obwod']}, Liczba pól: {dane['pola']}, Wynik: {dane['obwod']} * {dane['pola']} = {obwod_pomnozony}\n")
    obwody.append(str(obwod_pomnozony))  # Dodajemy wynik do listy jako string

# Sumowanie obwodów pomnożonych przez liczbę pól
suma = sum(int(x) for x in obwody)  # Zamieniamy na int, żeby sumować

# Formatowanie wyniku
obwody_polaczenia = " + ".join(obwody)  # Łączymy wyniki w jeden string

print(f"Całkowity wynik: {obwody_polaczenia} = {suma}\n")
