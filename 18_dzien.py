import sys
import numpy as np

def wczytaj_mape():
    print("Wklej tekst i naciśnij Enter dwukrotnie, aby zakończyć:")
    tekst = sys.stdin.read()
    lista = tekst.strip().split('\n')
    n_lista = [list(map(int, w.split(","))) for w in lista]
    return n_lista
    
def stworz_tablice(lista, dlugosc):
    tablica = np.zeros((7, 7), dtype=int)

    for i in range(dlugosc):
        x, y = lista[i]
        if 0 <= x < 7 and 0 <= y < 7:
            tablica[x][y] = 1

    return tablica

def pokaz_tablice(tablica):
    for wiersz in tablica:
        print(" ".join(map(str, wiersz)))

def policz_sasiadow(x, y, zajete_pola = []):
    ruchy = {1:(0, -1), 2:(1, 0), 3:(0, 1), 4:(-1, 0)}
    indexy_sasiadow = []
    for i in range(1, 5):
        a, b = ruchy[i][0], ruchy[i][1]
        try:
            if tablica[x + a][y + b] == 0:
                indexy_sasiadow.append((x + a, y + b))
        except IndexError:
            continue
        n_idx_sasiadow = []
    for i in range(len(indexy_sasiadow)):
        if indexy_sasiadow[i] not in zajete_pola:
            n_idx_sasiadow.append(indexy_sasiadow[i])

    return n_idx_sasiadow

def bfs(x, y, zajete_pola = []):
    sasiedzi = policz_sasiadow(x, y)


lista = wczytaj_mape()
mozliwaTrasa = True
dlugosc = 0

while mozliwaTrasa:
    dlugosc += 1
    tablica = stworz_tablice(lista, dlugosc)
    print(f"\nStan tablicy po {dlugosc} bajtach:")
    pokaz_tablice(tablica)
    szukajTrasy = bfs(0, 0)
    if not szukajTrasy:
        break

print(f"Znaleziono trasę, długość listy to: {dlugosc}")
