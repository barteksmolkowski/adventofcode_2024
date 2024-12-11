import time

mapa = [
    ">........#",
    ".#........",
    ".......#..",
    "...#......",
    ".....#....",
    "....#.....",
    "..#.......",
    "......#...",
    "#.........",
    "........#."
]

def usun_poprzednie():
    print("\n" * 30)

def znajdz_strzalke():
    for y in range(len(mapa)):
        for x in range(len(mapa[y])):

            if mapa[y][x] in ['^', '>', 'v', '<']:
                return x, y, mapa[y][x]
            
    return None, None, None

def usun_strzalke():
    global mapa

    for y in range(len(mapa)):
        mapa[y] = mapa[y].replace('^', '.').replace('>', '.').replace('v', '.').replace('<', '.')

x, y, kierunek = znajdz_strzalke()
kroki = 0

def rysuj_mape():
    usun_poprzednie()

    for i in range(len(mapa)):
        wiersz = list(mapa[i])

        if i == y:
            wiersz[x] = kierunek

        print(''.join(wiersz))

def wykonaj_ruch():
    global x, y, kierunek, kroki

    if kierunek in ["^", ">", "v", "<"]:
        kierunki = {"^" : (0, -1), ">" : (1, 0), "v" : (0, 1), "<" : (-1, 0)}
        a, b = kierunki[kierunek]

        if 0 <= y + b < len(mapa) and 0 <= x + a < len(mapa[0]):

            if mapa[y + b][x + a] != "#":

                x, y, kroki = x + a, y + b, kroki + 1

            else:
                slownik_kierunek = {"^": ">", ">": "v", "v": "<", "<": "^"}
                kierunek = slownik_kierunek.get(kierunek, kierunek)

        else:
            print(f"Koniec! Strzałka opuściła mapę po {kroki} krokach.")
            exit()

    print(kroki)

rysuj_mape()   
input("Klikni enter żeby rozpocząć chodzenie:\n")

while True:
    usun_strzalke()
    rysuj_mape()
    wykonaj_ruch()
    time.sleep(0.2)