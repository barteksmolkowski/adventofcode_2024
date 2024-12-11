mapa = [
    "89010123",
    "78121874",
    "87430965",
    "96549874",
    "45678903",
    "32019012",
    "01329801",
    "10456732"
]

def czujnik(x, y, p_start, odwiedzone):
    kierunki = {1: (-1, 0), 2: (0, 1), 3: (1, 0), 4: (0, -1)}
    p_obok = []
    for i in range(1, 5):
        a, b = kierunki[i]
        nx, ny = x + a, y + b
        if 0 <= nx < len(mapa) and 0 <= ny < len(mapa[0]):
            if mapa[nx][ny] == str(p_start + 1) and (nx, ny) not in odwiedzone:
                p_obok.append((nx, ny))
    return p_obok

def znajdz_zera():
    zera = []
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == "0":
                zera.append((i, j))
    return zera

def wyswietl_trasy(sciezki):
    for nr, trasa in sciezki.items():
        print(f"Trasa {nr + 1}: {trasa}")
        
wszyst_sciezki = {}
nr_sciezki = 0
zera = znajdz_zera()

for start_x, start_y in zera:
    wartosc = 0
    trasa = [(start_x, start_y)]
    odwiedzone = set(trasa)
    rozwidlenia = []

    while True:
        sasiedzi = czujnik(start_x, start_y, wartosc, odwiedzone)

        if len(sasiedzi) == 0:
            if wartosc == 9:
                wszyst_sciezki[nr_sciezki] = trasa[:]
                nr_sciezki += 1
            if rozwidlenia:
                start_x, start_y, wartosc, trasa = rozwidlenia.pop()
            else:
                break

        elif len(sasiedzi) == 1:
            start_x, start_y = sasiedzi[0]
            trasa.append((start_x, start_y))
            odwiedzone.add((start_x, start_y))
            wartosc += 1

        else:
            rozwidlenia.append((start_x, start_y, wartosc, trasa[:]))
            start_x, start_y = sasiedzi[0]
            trasa.append((start_x, start_y))
            odwiedzone.add((start_x, start_y))
            wartosc += 1

wyswietl_trasy(wszyst_sciezki)
print("Liczba tras:", len(wszyst_sciezki))