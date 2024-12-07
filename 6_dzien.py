mapa = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#..."
]

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
kroki = -1

def rysuj_mape():
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
        
        # Sprawdzanie, czy strzałka może wykonać ruch
        if 0 < y < len(mapa) - 1 and 0 < x < len(mapa[0]) - 1 and mapa[y + b][x + a] != "#":
            x += a
            y += b
            kroki += 1
        elif y == 0 or y == len(mapa) - 1 or x == 0 or x == len(mapa[0]) - 1:
            print(f"Koniec! Strzałka dotarła do granicy mapy po {kroki} krokach.")
            exit()  # Kończy działanie programu, gdy strzałka wyjdzie poza mapę
        else:
            # Zmiana kierunku strzałki (obrót w prawo)
            if kierunek == "^":
                kierunek = ">"
            elif kierunek == ">":
                kierunek = "v"
            elif kierunek == "v":
                kierunek = "<"
            elif kierunek == "<":
                kierunek = "^"

    print(kroki)

while True:
    usun_strzalke()
    rysuj_mape()
    if x < 0 or x >= len(mapa[0]) or y < 0 or y >= len(mapa):
        print(f"Koniec! Strzałka opuściła mapę po {kroki} krokach.")
        break
    wykonaj_ruch()
    input("Naciśnij Enter, aby kontynuować...")
