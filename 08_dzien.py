tablica = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............"
]

def mozliwosci(wartosci, dlugosc):
    if dlugosc != 2:
        return "Obsługiwane są tylko pary o długości 2."
    
    mozliwe = []

    for i in range(len(wartosci)):
        for j in range(i + 1, len(wartosci)):
            mozliwe.append((wartosci[i], wartosci[j]))
    
    return mozliwe

znaki = {}

for i in range(len(tablica)):
    for j in range(len(tablica[i])):
        znak = tablica[i][j]
        if znak == ".":
            continue
        if znak not in znaki:
            znaki[znak] = []
        znaki[znak].append((i, j))

tablica_z_antywezlami = [list(wiersz) for wiersz in tablica]

for z in znaki:
    liczby = znaki[z]
    tablica_par = mozliwosci(liczby, 2)
    
    for para in tablica_par:

        x1, y1 = para[0]
        x2, y2 = para[1]

        odleglosc_x, odleglosc_y = abs(x1 - x2), abs(y1 - y2)

        punkt_a_x, punkt_a_y = x1 - odleglosc_x, y1 - odleglosc_y
        punkt_b_x, punkt_b_y = x1 + odleglosc_x, y1 + odleglosc_y

        for punkt_x, punkt_y in [(punkt_a_x, punkt_a_y), (punkt_b_x, punkt_b_y)]:
            if 0 <= punkt_x < len(tablica) and 0 <= punkt_y < len(tablica[0]) and tablica_z_antywezlami[punkt_x][punkt_y] == ".":
                tablica_z_antywezlami[punkt_x][punkt_y] = "#"

for wiersz in tablica_z_antywezlami:
    print("".join(wiersz))