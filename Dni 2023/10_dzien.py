tablica = [
    "..F7.",
    ".FJ|.",
    "SJ.L7",
    "|F--J",
    "LJ..."
]

def ZnajdzStart():
    for i in range(len(tablica)):
        for j in range(len(tablica[i])):
            if tablica[i][j] == "S":
                return i, j
    return None

def ZnajdzKierunki(znak):
    kierunki = {
        "|": [(-1, 0), (1, 0)],
        "-": [(0, -1), (0, 1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
        "S": [(0, -1), (0, 1), (-1, 0), (1, 0)],
        ".": []
    }
    return kierunki.get(znak, [])

def CzyPolaczenie(znak1, znak2, dx, dy):
    kierunki1 = ZnajdzKierunki(znak1)
    kierunki2 = ZnajdzKierunki(znak2)
    return (dx, dy) in kierunki1 and (-dx, -dy) in kierunki2

def IdzTrasa():
    start = ZnajdzStart()
    if start is None:
        print("Nie znaleziono punktu startowego.")
        return

    odwiedzone = set()
    trasa = []
    stos = [start]
    print(f"Start w punkcie: {start}")

    while stos:
        x, y = stos.pop()
        if (x, y) in odwiedzone:
            continue

        odwiedzone.add((x, y))
        trasa.append((x, y))
        print(f"Odwiedzono: ({x}, {y}), znak: {tablica[x][y]}")

        # Sprawdzanie sąsiadów w dozwolonych kierunkach
        for dx, dy in ZnajdzKierunki(tablica[x][y]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(tablica) and 0 <= ny < len(tablica[0]):  # Sprawdź, czy w granicach
                if (nx, ny) not in odwiedzone and CzyPolaczenie(tablica[x][y], tablica[nx][ny], dx, dy):
                    stos.append((nx, ny))

    print(f"Trasa zwierzęcia: {trasa}")
    return trasa

# Wywołanie funkcji
IdzTrasa()
