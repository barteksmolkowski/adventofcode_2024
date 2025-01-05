def znajdz_numery_slownik(tablica):
    liczba = 0
    kordyLiczby = []
    liczby_slownik = {}

    for i in range(len(tablica)):
        wiersz = tablica[i][0]
        for j, znak in enumerate(wiersz):
            pole = (i, j)
            if znak.isdigit():
                liczba = liczba * 10 + int(znak)
                kordyLiczby.append(pole)
            else:
                if liczba != 0:
                    liczby_slownik[liczba] = kordyLiczby
                liczba = 0
                kordyLiczby = []

        if liczba != 0:
            liczby_slownik[liczba] = kordyLiczby
            liczba = 0
            kordyLiczby = []

    return liczby_slownik

def OdkryjSasiadow(pole, tablica):
    x, y = pole
    symbole = ["*", "#", "+", "$"]
    
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            a, b = x + i, y + j
            try:
                if tablica[a][0][b] in symbole:
                    return False
            except IndexError:
                continue
    return True

tablica = [
    ["467..114.."],
    ["...*......"],
    ["..35..633."],
    ["......#..."],
    ["617*......"],
    [".....+.58."],
    ["..592....."],
    ["......755."],
    ["...$.*...."],
    [".664.598.."]
]

slownik_liczb = znajdz_numery_slownik(tablica)
liczby = []

for liczba, kordy in slownik_liczb.items():
    czy_czesci = True
    for pole in kordy:
        if not OdkryjSasiadow(pole, tablica):
            czy_czesci = False
            break
    if czy_czesci:
        liczby.append(liczba)

print(f"Liczby które nie sąsiadują ze znakami: ")
