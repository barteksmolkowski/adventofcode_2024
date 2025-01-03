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
    liczba = 0
    klucz = tablica[x][y]
    for i in range(1, 5):
        a, b = kierunki[i]

        if 0 <= x + a < len(tablica) and 0 <= y + b < len(tablica[0]) and tablica[x + a][y + b] == klucz:
            liczba += 1

    return klucz, liczba

elementy = {}

for i in range(len(tablica)):
    for j in range(len(tablica[i])):

        klucz, liczba = jaki_elem(i, j)
        
        if klucz not in elementy:
            elementy[klucz] = {'obwod': 0, 'pola': 0}
        
        obwod = 4 - liczba
        elementy[klucz]['obwod'] += obwod
        elementy[klucz]['pola'] += 1

obwody = []
for klucz, dane in elementy.items():
    obwod_pomnozony = dane['obwod'] * dane['pola']
    print(f"Litera: {klucz} Obwody: {dane['obwod']}, Liczba pól: {dane['pola']}, Wynik: {dane['obwod']} * {dane['pola']} = {obwod_pomnozony}\n")
    obwody.append(str(obwod_pomnozony))

suma = sum(int(x) for x in obwody)

obwody_polaczenia = " + ".join(obwody)

print(f"Całkowity wynik: {obwody_polaczenia} = {suma}\n")
