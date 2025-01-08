tablica = [
    [-1, 0, 0],
    [0, 1, 0],
    [0, 0, 2]
]

x, y = 0, 0  # Start

def bfs(x, y):
    def policz_sasiadow(x, y, zajete_pola):
        ruchy = {1: (0, -1), 2: (1, 0), 3: (0, 1), 4: (-1, 0)}
        indexy_sasiadow = []
        for dx, dy in ruchy.values():
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(tablica) and 0 <= ny < len(tablica[0]):  # Sprawdź czy w granicach
                if tablica[nx][ny] != 1 and (nx, ny) not in zajete_pola:  # Blokada lub już zajęte
                    indexy_sasiadow.append((nx, ny))
        return indexy_sasiadow

    # Inicjalizacja BFS
    kolejka = [(x, y, [(x, y)])]  # Kolejka: (bieżący x, bieżący y, ścieżka)
    licznik_sciezek = 0

    while kolejka:
        cx, cy, sciezka = kolejka.pop(0)

        # Jeśli dotarliśmy do celu (wartość 2)
        if tablica[cx][cy] == 2:
            licznik_sciezek += 1
            continue

        # Znajdź sąsiadów i dodaj do kolejki
        sasiedzi = policz_sasiadow(cx, cy, sciezka)
        for nx, ny in sasiedzi:
            kolejka.append((nx, ny, sciezka + [(nx, ny)]))

    return licznik_sciezek

print(bfs(x, y))  # Wynik: liczba możliwych tras
