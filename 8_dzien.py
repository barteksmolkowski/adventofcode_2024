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
    if dlugosc != 2:  # Obsługujemy tylko długość 2 w tej wersji
        return "Obsługiwane są tylko pary o długości 2."
    
    mozliwe = []
    
    # Tworzenie par
    for i in range(len(wartosci)):
        for j in range(i + 1, len(wartosci)):
            mozliwe.append((wartosci[i], wartosci[j]))
    
    return mozliwe

# Zbieramy pozycje każdego znaku
znaki = {}

for i in range(len(tablica)):
    for j in range(len(tablica[i])):
        znak = tablica[i][j]
        if znak == ".":  # Ignorujemy puste pola
            continue
        if znak not in znaki:
            znaki[znak] = []  # Tworzymy nową listę dla nowego znaku
        znaki[znak].append((i, j))  # Dodajemy pozycję do listy

# Modyfikujemy tablicę, aby dodać antywęzły
tablica_z_antywezlami = [list(wiersz) for wiersz in tablica]  # Kopiujemy tablicę do modyfikacji

# Sprawdzamy pary dla każdego znaku
for z in znaki:
    liczby = znaki[z]
    tablica_par = mozliwosci(liczby, 2)
    for para in tablica_par:
        # Pobieramy pozycje dwóch anten
        x1, y1 = para[0]
        x2, y2 = para[1]
        
        # Obliczamy odległość między antenami
        odleglosc_x = abs(x1 - x2)
        odleglosc_y = abs(y1 - y2)
        
        # Obliczamy pozycje antywęzłów po obu stronach anten
        punkt_a_x, punkt_a_y = x1 - odleglosc_x, y1 - odleglosc_y
        punkt_b_x, punkt_b_y = x1 + odleglosc_x, y1 + odleglosc_y
        
        # Sprawdzamy, czy pozycje antywęzłów są w granicach mapy
        # I czy pole jest puste, aby dodać #
        if 0 <= punkt_a_x < len(tablica) and 0 <= punkt_a_y < len(tablica[0]):
            if tablica_z_antywezlami[punkt_a_x][punkt_a_y] == ".":
                tablica_z_antywezlami[punkt_a_x][punkt_a_y] = "#"  # Dodajemy antywęzeł
            
        if 0 <= punkt_b_x < len(tablica) and 0 <= punkt_b_y < len(tablica[0]):
            if tablica_z_antywezlami[punkt_b_x][punkt_b_y] == ".":
                tablica_z_antywezlami[punkt_b_x][punkt_b_y] = "#"  # Dodajemy antywęzeł

# Wyświetlamy mapę z antywęzłami
for wiersz in tablica_z_antywezlami:
    print("".join(wiersz))