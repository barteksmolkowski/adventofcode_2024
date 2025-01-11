Dane = [
    ("R", 6, "#70c710"),
    ("D", 5, "#0dc571"),
    ("L", 2, "#5713f0"),
    ("D", 2, "#d2c081"),
    ("R", 2, "#59c680"),
    ("D", 2, "#411b91"),
    ("L", 5, "#8ceee2"),
    ("U", 2, "#caa173"),
    ("L", 1, "#1b58a2"),
    ("U", 2, "#caa171"),
    ("R", 2, "#7807d2"),
    ("U", 3, "#a77fa3"),
    ("L", 2, "#015232"),
    ("U", 2, "#7a21e3")
]

KIERUNKI = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}

def StworzTab(dane):
    MaxWys, MaxSzer, AktX, AktY = 0, 0, 0, 0
    pola = []  # Lista odwiedzonych pól
    KIERUNKI = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}

    for ruch in dane:
        kierunek, kroki, _ = ruch
        StareX, StareY = AktX, AktY
        AktX += KIERUNKI[kierunek][0] * kroki
        AktY += KIERUNKI[kierunek][1] * kroki

        # Dodajemy współrzędne śladu między punktami
        for i in range(kroki + 1):  # Od początku do końca ruchu
            x = StareX + i * KIERUNKI[kierunek][0]
            y = StareY + i * KIERUNKI[kierunek][1]
            pola.append((x, y))

        # Aktualizacja maksymalnych/minimalnych wartości
        MaxWys, MaxSzer = max(MaxWys, AktX), max(MaxSzer, AktY)

    # Tworzenie tablicy z przesunięciem współrzędnych
    wysokosc = MaxWys + 1
    szerokosc = MaxSzer + 1
    tablica = [["." for _ in range(szerokosc)] for _ in range(wysokosc)]

    # Rysowanie odwiedzonych pól
    for x, y in pola:
        tablica[x][y] = "#"

    return tablica

tablica, pola = StworzTab(Dane)

# Wyświetlanie tablicy
for row in tablica:
    print("".join(row))

# Wyświetlanie odwiedzonych pól
print(pola)