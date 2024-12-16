# Labirynt
tablica = [
    list("###############"),
    list("#.......#....E#"),
    list("#.#.###.#.###.#"),
    list("#.....#.#...#.#"),
    list("#.###.#####.#.#"),
    list("#.#.#.......#.#"),
    list("#.#.#####.###.#"),
    list("#...........#.#"),
    list("###.#.#####.#.#"),
    list("#...#.....#.#.#"),
    list("#.#.#.###.#.#.#"),
    list("#.....#...#.#.#"),
    list("#.###.#.#.#.#.#"),
    list("#S..#.....#...#"),
    list("###############")
]

pozycja_startowa, pozycja_meta = (1, 1), (1, 13)
kierunki = {1: (0, -1), 2: (1, 0), 3: (0, 1), 4: (-1, 0)}

def bfs(pozycja_startowa, pozycja_meta):
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

długość_trasy = bfs(pozycja_startowa, pozycja_meta)

if długość_trasy != -1:
    print(f"Najkrótsza trasa ma długość {długość_trasy}")
else:
    print("Brak ścieżki do mety.")