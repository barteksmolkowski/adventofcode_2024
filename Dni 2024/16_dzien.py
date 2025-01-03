import sys

def wczytaj_mape():
    print("Wklej labirynt (każdy wiersz w osobnej linii), a następnie naciśnij dwa razy Enter:")
    labirynt = sys.stdin.read()  # Wczytanie całego wejścia
    linie = labirynt.strip().splitlines()  # Podziel wejście na linie
    
    tablica = []
    pozycja_startowa = pozycja_meta = None  # Zmienna na pozycje startowe i mety
    
    for wiersz, linia in enumerate(linie):
        tablica.append(list(linia.strip()))
        
        # Szukamy 'S' (start) i 'M' (meta) w każdej linii
        for kolumna in range(len(linia)):
            if linia[kolumna] == 'S':
                pozycja_startowa = (wiersz, kolumna)  # Zapisujemy pozycję startu
            elif linia[kolumna] == 'E':
                pozycja_meta = (wiersz, kolumna)  # Zapisujemy pozycję mety
    
    # Jeśli nie znaleziono 'S' lub 'M', możemy zgłosić błąd
    if pozycja_startowa is None or pozycja_meta is None:
        print("Nie znaleziono punktów startowego (S) lub mety (M) w labiryncie!")
        return None, None, None  # Zwracamy None, aby sygnalizować błąd
    
    return tablica, pozycja_startowa, pozycja_meta  # Zwracamy mapę oraz pozycje startowe i mety

def drukuj_labyrynt(tablica):
    for wiersz in tablica:
        print("".join(wiersz))

def bfs(pozycja_startowa, pozycja_meta, tablica):
    kierunki = {1: (0, -1), 2: (1, 0), 3: (0, 1), 4: (-1, 0)}
    
    kolejka = [(pozycja_startowa, 0)]
    odwiedzone = set()
    odwiedzone.add(pozycja_startowa)
    
    while kolejka:
        (x, y), głębokość = kolejka.pop(0)
        print(f"Sprawdzanie trasy: {x}, {y} (głębokość: {głębokość})")
        
        if (x, y) == pozycja_meta:
            return głębokość
        
        for dx, dy in kierunki.values():
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < len(tablica) and 0 <= ny < len(tablica[0]) and tablica[nx][ny] != "#" and (nx, ny) not in odwiedzone:
                odwiedzone.add((nx, ny))
                kolejka.append(((nx, ny), głębokość + 1))
    
    return -1

tablica, pozycja_startowa, pozycja_meta = wczytaj_mape()

if tablica is None:
    exit()

print("\n" * 30)
drukuj_labyrynt(tablica)

długość_trasy = bfs(pozycja_startowa, pozycja_meta, tablica)

if długość_trasy != -1:
    print(f"Najkrótsza trasa ma długość {długość_trasy}")
else:
    print("Brak ścieżki do mety.")