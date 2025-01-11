def PoliczSasiadow(x, y, zajetePola=set()):
    sasiedzi = []
    kierunki = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in kierunki:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(tablica) and 0 <= ny < len(tablica[0]) and (nx, ny) not in zajetePola:
            sasiedzi.append((nx, ny))
    return sasiedzi

def Algorytmbfs(startX, startY, trasy=[], zajetePola=set()):
    zajetePola = set(zajetePola)
    if not trasy:
        sasiedzi = PoliczSasiadow(startX, startY, zajetePola)
        for sasiad in sasiedzi:
            trasy.append([sasiad])
            zajetePola.add(sasiad)

    NoweTrasy = []

    for trasa in trasy:
        x, y = trasa[-1]
        zajetePola_trasa = set(trasa)  # Dodajemy wszystkie punkty tej trasy do zbioru
        sasiedzi = PoliczSasiadow(x, y, zajetePola_trasa)

        for sasiad in sasiedzi:
            if sasiad not in zajetePola_trasa:
                NowaTrasa = trasa + [sasiad]
                NoweTrasy.append(NowaTrasa)

    # Usunięcie tras zawierających powtórki punktów
    FiltrowaneTrasy = [trasa for trasa in NoweTrasy if len(trasa) == len(set(trasa))]

    # Usunięcie tras zawierających (0, 0)
    FiltrowaneTrasy = [trasa for trasa in FiltrowaneTrasy if (0, 0) not in trasa]

    return FiltrowaneTrasy

def WyswietlTrase(Trasa):
    NowaTab = []
    for i in range(len(tablica)):
        NowyWiersz = []
        for j in range(len(tablica[i])):
            if (i, j) in Trasa:
                NowyWiersz.append(tablica[i][j])
            else:
                NowyWiersz.append("x")
        NowaTab.append(NowyWiersz)

    for row in NowaTab:
        print(" ".join(row))

def bfs(startX, startY, zajetePola, powtorka=1):
    minSum = float('inf')
    minTrasa = None
    trasy = []

    for i in range(powtorka):
        trasy = Algorytmbfs(startX, startY, trasy, zajetePola)
        # print(f"Głębokość algorytmu: {i}, liczba tras: {len(trasy)}")
        # print(f"Trasy: {trasy}")

    # trasyZkoncem = [trasa for trasa in trasy if trasa[-1] == (3, 3)]
    trasy = [[(0, 0)] + trasa for trasa in trasy]

    for trasa in trasy:
        liczba = 0
        for j in range(len(trasa)):
            x, y = trasa[j]
            liczba += int(tablica[x][y])
        if liczba < minSum:
            minSum = liczba
            minTrasa = trasa
        # print(f"Trasa: {trasa}, suma: {liczba}")
    print(f"\nNajmniejsza trasa to: {minTrasa}")
    print(f"Minimalna suma wartości pól dla tras: {minSum}")
    pole = (minTrasa[-1][0], minTrasa[-1][0])
    return minSum, minTrasa, pole

# Tablica
tablica = [
    list("2413432311323"),
    list("3215453535623"),
    list("3255245654254"),
    list("3446585845452"),
    list("4546657867536"),
    list("1438598798454"),
    list("4457876987766"),
    list("3637877979653"),
    list("4654967986887"),
    list("4564679986453"),
    list("1224686865563"),
    list("2546548887735"),
    list("4322674655533"),
]

# Wykonanie
punkty, minTrasa, pole = bfs(0, 0, set(), powtorka=10)
x, y = pole
print(f"end, punkty:({punkty}), minTrasa:({minTrasa})")
x, y = minTrasa[-1]
WyswietlTrase(minTrasa)

punkty, minTrasa, pole = bfs(x, y, minTrasa, powtorka=10)
x, y = pole
print(f"end, punkty:({punkty}), minTrasa:({minTrasa})")
x, y = minTrasa[-1]
WyswietlTrase(minTrasa)

