tablica = [
    "...........",
    ".....###.#.",
    ".###.##..#.",
    "..#.#...#..",
    "....#.#....",
    ".##..S####.",
    ".##..#...#.",
    ".......##..",
    ".##.#.####.",
    ".##..##.##.",
    "..........."
]

def ZnajdzS():
    for i in range(len(tablica)):
        for j in range(len(tablica[i])):
            if tablica[i][j] == "S":
                return i, j

def SprawdzSasiadow(x, y):
    sasiedzi = []
    kierunki = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    for a, b in kierunki.values():
        try:
            Nx, Ny = x + a, y + b
            if 0 <= Nx < len(tablica) and 0 <= Ny < len(tablica[0]) and tablica[Nx][Ny] == ".":
                sasiedzi.append((Nx, Ny))
        except IndexError:
            continue
    return sasiedzi

def bfs(Punkty_startowe=None, WszystkieOdkryte=None):
    if Punkty_startowe is None:
        x_start, y_start = ZnajdzS()
        Punkty_startowe = [(x_start, y_start)]
    
    if WszystkieOdkryte is None:
        WszystkieOdkryte = set(Punkty_startowe)

    NoweOdkrPunkty = []

    for x, y in Punkty_startowe:
        sasiedzi = SprawdzSasiadow(x, y)

        for sasied in sasiedzi:
            if sasied not in WszystkieOdkryte:
                NoweOdkrPunkty.append(sasied)
                WszystkieOdkryte.add(sasied)

    return NoweOdkrPunkty, WszystkieOdkryte

def SprawdzMape(odkryte_punkty):
    zajete_pola = len(odkryte_punkty)
    wolne_pola = sum(row.count('.') for row in tablica) - zajete_pola

    print(f"Zajętych: {zajete_pola}. Wolnych: {wolne_pola}")
    if wolne_pola == 0:
        return True
    else:
        return False


def ProgramBFS():
    OdkrytePunkty = set()
    PunktyDoSprawdzenia = None
    GlebokośćLabiryntu = 0

    while not SprawdzMape(OdkrytePunkty) and GlebokośćLabiryntu < 130:
        input("Wciśnij Enter, aby kontynuować...")
        GlebokośćLabiryntu += 1
        PunktyDoSprawdzenia, OdkrytePunkty = bfs(PunktyDoSprawdzenia, OdkrytePunkty)

        print(f"Odkryte punkty: {sorted(OdkrytePunkty)}")
        print(f"Sprawdzana głębokość: {GlebokośćLabiryntu}")
        RysujTablica(OdkrytePunkty)

    return GlebokośćLabiryntu


def RysujTablica(odkryte_punkty=[]):
    widok = [list(wiersz) for wiersz in tablica]

    for x, y in odkryte_punkty:
        widok[x][y] = 'X'

    for wiersz in widok:
        print("".join(wiersz))

GlebokośćLabiryntu = ProgramBFS()
print(f"Policzono do głębokości: {GlebokośćLabiryntu}")