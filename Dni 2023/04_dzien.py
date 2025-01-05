tablica = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

def sprawdz(liczbyWin, LiczbyZwykle):
    dopasowania = set(liczbyWin) & set(LiczbyZwykle)
    return 2 ** len(dopasowania) - 1 if dopasowania else 0

punkty = 0

for i in range(len(tablica)):
    wiersz = tablica[i][8:]
    liczbyWin = []
    liczba = 0

    for j in range(15):
        try:
            liczba = liczba * 10 + int(wiersz[j])
        except ValueError:
            if liczba != 0:
                liczbyWin.append(liczba)
                liczba = 0

    liczba = 0
    wiersz = wiersz[17:]
    LiczbyZwykle = []

    for j in range(23):
        try:
            liczba = liczba * 10 + int(wiersz[j])
        except ValueError:
            if liczba != 0:
                LiczbyZwykle.append(liczba)
                liczba = 0

    LiczbyZwykle.append(liczba)

    punkty += sprawdz(liczbyWin, LiczbyZwykle)

print(punkty)