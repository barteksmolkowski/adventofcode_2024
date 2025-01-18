from typing import List, Optional

tablica = [
    "#.#####################",
    "#.......#########...###",
    "#######.#########.#.###",
    "###.....#.>.>.###.#.###",
    "###v#####.#v#.###.#.###",
    "###.>...#.#.#.....#...#",
    "###v###.#.#.#########.#",
    "###...#.#.#.......#...#",
    "#####.#.#.#######.#.###",
    "#.....#.#.#.......#...#",
    "#.#####.#.#.#########v#",
    "#.#...#...#...###...>.#",
    "#.#.#v#######v###.###v#",
    "#...#.>.#...>.>.#.###.#",
    "#####v#.#.###v#.#.###.#",
    "#.....#...#...#.#.#...#",
    "#.#########.###.#.#.###",
    "#...###...#...#...#.###",
    "###.###.#.###v#####v###",
    "#...#...#.#.>.>.#.>.###",
    "#.###.###.#.###.#.#v###",
    "#.....###...###...#...#",
    "#####################.#"
]

def PokażPunkty(lista: List):
    NowaTablica = [list(wiersz) for wiersz in tablica]
    for (x, y) in lista:
        NowaTablica[x][y] = "X"
    for wiersz in NowaTablica:
        print(''.join(wiersz))

def ZnajdzSasiadów(x: int, y: int, unikajPól: Optional[List]):
    sasiedzi = []
    kierunki = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    blockKierunki = {0: "v", 1: "<", 2: "^", 3: ">"}
    
    for i in kierunki:
        dx, dy = kierunki[i]
        Nx, Ny = x + dx, y + dy
        zablokowany = blockKierunki[i]

        if 0 <= Nx < len(tablica) and 0 <= Ny < len(tablica[0]):
            if tablica[Nx][Ny] in [".", ">", "v", "<", "^"]:
                if tablica[Nx][Ny] != zablokowany and (Nx, Ny) not in unikajPól:
                    sasiedzi.append((Nx, Ny))
    
    return sasiedzi

def ZnajdzStart():
    for x, line in enumerate(tablica):
        for y, value in enumerate(line):
            if value == '.':
                return (x, y)
    return (-1, -1)

def dfsTrasowe(Trasy: Optional[List[List[tuple]]] = None):
    WszystkieTrasy = []
    if Trasy is None:
        Trasy = []
        x, y = ZnajdzStart()
        Trasy.append([(x, y)])
    
    while Trasy:
        trasa = Trasy.pop()
        StartX, StartY = trasa[-1]
        
        sasiedzi = ZnajdzSasiadów(StartX, StartY, trasa)
        
        if not sasiedzi:
            WszystkieTrasy.append(trasa)
        else:
            for sasiad in sasiedzi:
                NowaTrasa = trasa + [sasiad]
                Trasy.append(NowaTrasa)
    
    print(f"Znalezione wszystkie trasy: {WszystkieTrasy}")
    return WszystkieTrasy

trasy = dfsTrasowe()
NajdłuższaTrasa = []

for trasa in trasy:
    trasa.pop(0)


for i, trasa in enumerate(trasy):
    print(f"Trasa nr.{i} ma kratek: {len(trasa)}")
    if len(trasa) > len(NajdłuższaTrasa):
        NajdłuższaTrasa = trasa

print(f"Najdłuższa trasa ({len(NajdłuższaTrasa)} kratek):")
PokażPunkty(NajdłuższaTrasa)
